from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import ArticlePost


def list_article(request):
    content = {'articles': ArticlePost.objects.all()}
    return render(request, 'article/list.html', content)
