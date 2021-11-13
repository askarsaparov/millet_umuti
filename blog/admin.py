from django.contrib import admin

from blog.models import Tag, Profile, Article

admin.site.register(Tag)
admin.site.register(Profile)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('headline',),}

admin.site.site_header = "Millet u'miti - Admin"
admin.site.site_title = "Millet u'miti - Admin"
admin.site.index_title = "Millet u'miti - Admin"