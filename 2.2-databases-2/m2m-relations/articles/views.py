from django.shortcuts import render
from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    news = Article.objects.prefetch_related('tag').all()
    context = {
        'object_list': news,

    }



    return render(request, template, context)
