from django.urls import path

from blog.views import home, article, articles, tag_articles


urlpatterns = [
    path('', home, name='home'),
    path('articles/', articles, name='articles'),
    path('tag/<str:tag>/', tag_articles, name='tag_articles'),
    path('<slug:article>/', article, name='article'),
]