from django.db import models

class Cars(models.Model):
    brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    date_of_production = models.CharField('Year of Production', max_length=4)
    create_time = models.DateTimeField('create time', auto_now_add=True)
    last_edit_time = models.DateTimeField('last edit time', auto_now=True)
