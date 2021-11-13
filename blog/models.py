from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField

class Profile(models.Model):

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Atin`iz')
    last_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Familiyan`iz')
    email = models.CharField(max_length=200)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='profile', verbose_name='profil su`wret')
    bio = models.TextField(null=True, blank=True, verbose_name='qisqasha ma`luwmat')
    twitter = models.URLField(max_length=200, null=True, blank=True, verbose_name='soccial tarmaq linki')

    def __str__(self):
        name = str(self.first_name)
        if self.last_name:
            name += ' ' + str(self.last_name)
        return name


class ArticleManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):

    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='author', verbose_name='Avtor')

    headline = models.CharField(max_length=200, verbose_name='Atama')
    sub_headline = models.CharField(max_length=200, null=True, blank=True, verbose_name='qosimsha atama')
    image = models.ImageField(null=True, blank=True, upload_to='article', default='placeholder.png', verbose_name='Poster su`wreti')
    body = RichTextUploadingField(null=True, blank=True, verbose_name='text')
    featured = models.BooleanField(default=False, verbose_name='Aktual maqalalarg`a qosiw')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='teg')

    options = (
        ('draft', 'Qaralama'),
        ('published', 'Baspa')
    )
    slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name='link')
    publish = models.DateTimeField(default=timezone.now, verbose_name='baspa waqti')

    status = models.CharField(max_length=10, choices=options, default='draft')

    objects = models.Manager() #defaul Manager
    articleManager = ArticleManager() #custom Manager

    def get_absolute_url(self):
        return reverse('article', args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.headline
