from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("To jest pierwsza aplikacja")

# Create your views here.
