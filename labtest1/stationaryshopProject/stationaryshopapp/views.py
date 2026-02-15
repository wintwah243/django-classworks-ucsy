from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Product
from .forms import StationaryForm



# this is dev branch

# Create your views here.
def new(request):
    if request.method == 'POST':
        stationary_form = StationaryForm(request.POST)

        if stationary_form.is_valid():
            stationary_form.save()
            return HttpResponseRedirect('/')
    else:
        stationary_form = StationaryForm()

    return render(request, 'stationary/add.html', {'form': stationary_form})



def stationary(request):
    data = Product.objects.all()
    return render(request, 'stationary/stationary.html', {'stationaries': data})

def update(request, id):
    data = Product.objects.get(id=id)

    if request.method == 'POST':
        form = StationaryForm(request.POST, instance=data)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
            form = StationaryForm(instance=data)

    return render(request, 'stationary/update.html', {'form': form})



def delete(request, id):
    Product.objects.get(id=id).delete()
    return HttpResponseRedirect('/')