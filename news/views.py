from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
    news = News.objects.order_by('-create_time')

    context = {'news': news}

    return render(request, 'news/index.html', context)
# Create your views here.
