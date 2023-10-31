from django.shortcuts import render, redirect, get_object_or_404
from .models import Cars
from .forms import CarsForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.

def view_cars(request):
    cars = Cars.objects.order_by('-create_time')
    context = {'cars': cars}
    return render(request, 'cars/index.html', context)

@login_required(login_url='/login/')
def add_cars(request):
    if request.method == 'POST':
        cars = CarsForm(request.POST)

        if cars.is_valid():
            cars = cars.save(commit=False)
            cars.create_time = timezone.now()
            cars.last_edit_time = timezone.now()
            cars.save()
            return redirect('view_cars')

        else:
            context = {'form': cars}
            return render(request, 'cars/add.html', context)
    
    else:
        cars = CarsForm()
        context = {'form': cars}
        return render(request, 'cars/add.html', context)
    
def get(request, id):
    cars = get_object_or_404(Cars, id=id)
    context = {'cars': cars}
    return render(request, 'cars/view.html', context) 

@login_required(login_url='/login/')
def edit_news(request, cars_id):
    cars_item = get_object_or_404(Cars, pk=cars_id)

    if request.method == 'POST':
        form = CarsForm(request.POST, instance=cars_item)

        if form.is_valid():
            form.last_edit_time = timezone.now()
            form.save()
            return redirect('view_cars')  
    
    else:
        form = CarsForm(instance=cars_item)

    return render(request, 'cars/edit.html', {'form': form}) 