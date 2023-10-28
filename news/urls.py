from django.urls import path
from .views import index, add

urlpatterns = [
    path('', index, name='view_news'),
    path('add/', add, name='add')
]