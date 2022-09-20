from django.shortcuts import render
import pprint
from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    news = Article.objects.all()
    context = {
        'object_list': news,

    }



    return render(request, template, context)
