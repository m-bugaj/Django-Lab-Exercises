from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("News")
# Create your views here.
