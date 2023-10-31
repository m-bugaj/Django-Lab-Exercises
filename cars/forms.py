from django import forms
from .models import Cars

class CarsForm(forms.ModelForm):
    YEAR_CHOICES = [(str(year), str(year)) for year in range(2023, 1899, -1)]

    class Meta:
        model = Cars
        fields = ['brand', 'car_model', 'date_of_production']

    date_of_production = forms.ChoiceField(
        label='Year of Production',
        choices=YEAR_CHOICES,
        required=True,
    )
