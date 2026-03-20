from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Practice3
from .forms import Practice3Form


# Create your views here.

def new(request):
    if request.method == "POST":
        practice3form = Practice3Form(request.POST)

        if practice3form.is_valid():
            practice3form.save()
            return HttpResponseRedirect("/")
    else:
        practice3form = Practice3Form()

    return render(request, "practice3app/add.html", {"practice3form": practice3form})


def practice3(request):
    data = Practice3.objects.all()
    return render(request, "practice3app/practice3.html", {"practice3data": data})

def update(request, id):
    data = Practice3.objects.get(id=id)

    if request.method == "POST":
        practice3form = Practice3Form(request.POST, instance=data)

        if practice3form.is_valid():
            practice3form.save()
            return HttpResponseRedirect("/")
        else:
            practice3form = Practice3Form(instance=data)

    return render(request, "practice3app/update.html", {"practice3form": Practice3Form})

def delete(request, id):
    Practice3.objects.get(id=id).delete()
    return HttpResponseRedirect("/")
