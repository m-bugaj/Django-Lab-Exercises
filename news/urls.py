from django.urls import path
from .views import index, add, get, edit_news

urlpatterns = [
    path('', index, name='view_news'),
    path('add/', add, name='add'),
    path('<int:id>/', get, name='get'),
    path('edit/<int:news_id>/', edit_news, name='edit_news')
]