from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Medicine
from .forms import PharmacyForm


# Create your views here.
def new(request):
    if request.method == 'POST':
        pharmacy_form = PharmacyForm(request.POST)

        if pharmacy_form.is_valid():
            pharmacy_form.save()
            return HttpResponseRedirect('/')
    else:
        pharmacy_form = PharmacyForm()

    return render(request, 'pharmacy/add.html', {'form': PharmacyForm})



def pharmacy(request):
    data = Medicine.objects.all()
    return render(request, 'pharmacy/pharmacy.html', {'pharmacries': data})

def update(request, id):
    data = Medicine.objects.get(id=id)

    if request.method == 'POST':
        form = PharmacyForm(request.POST, instance=data)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
            form = PharmacyForm(instance=data)

    return render(request, 'pharmacy/update.html', {'form': form})



def delete(request, id):
    Medicine.objects.get(id=id).delete()
    return HttpResponseRedirect('/')