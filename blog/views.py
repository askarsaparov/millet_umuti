from django.db.models import Q
from django.shortcuts import render, HttpResponse, get_object_or_404

from blog.models import Article, Tag, Profile

def home(request):
    featured = Article.articleManager.filter(featured=True)[0:3]

    context = {
        'articles': featured,
    }
    return render(request, 'index.html', context)


def article(request, article):
    article = get_object_or_404(Article, slug=article, status='published')
    context = {
        'article': article
    }
    return render(request, 'article.html', context)


def articles(request):
    #get query from request
    query = request.GET.get('query')
    if query == None:
        query = ''

    # articles = Article.articleManager.all()
    #search for headline, sub headline, body
    articles = Article.articleManager.filter(
        Q(headline__icontains=query) |
        Q(sub_headline__icontains=query) |
        Q(body__icontains=query)
    )

    tags = Tag.objects.all()
    context = {
        'articles': articles,
        'tags': tags,
    }

    return render(request, 'articles.html', context)

def tag_articles(request, tag):

    tages = Tag.objects.get(name=tag)
    article = Article.objects.all()
    articles = tages.article_set.all()
    context = {
        'articles': articles,
        'tag': tages,
    }

    return render(request, 'tag_articles.html', context)