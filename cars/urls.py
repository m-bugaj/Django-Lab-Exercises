from django.urls import path
from .views import view_cars, add_cars, get, edit_news

urlpatterns = [
    path('', view_cars, name='view_cars'),
    path('add/', add_cars, name = 'add_cars'),
    path('<int:id>/', get, name='get'),
    path('edit/<int:cars_id>/', edit_news, name='edit_news'),
]