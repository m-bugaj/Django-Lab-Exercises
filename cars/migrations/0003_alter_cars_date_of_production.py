# Generated by Django 4.2.6 on 2023-10-31 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_cars_create_time_alter_cars_date_of_production_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='date_of_production',
            field=models.CharField(max_length=4, verbose_name='Year of Production'),
        ),
    ]