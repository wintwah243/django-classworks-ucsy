from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import Practice4Form
from .models import Practice4


# Create your views here.
def new(request):
    if request.method == "POST":
        practice4form = Practice4Form(request.POST)
        if practice4form.is_valid():
            practice4form.save()
            return HttpResponseRedirect("/")
        else:
            practice4form = Practice4Form()

    return render(request, "practice4app/add.html", {"form": Practice4Form})


def practice4(request):
    data = Practice4.objects.all()
    return render(request, "practice4app/practice4.html", {"practice4data": data})

def update(request, id):
    data = Practice4.objects.get(id=id)

    if request.method == "POST":
        form = Practice4Form(request.POST, instance=data)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            form = Practice4Form(instance=data)

    return render(request, "practice4app/update.html", {"form": Practice4Form})

def delete(request, id):
    Practice4.objects.get(id=id).delete()
    return HttpResponseRedirect("/")
