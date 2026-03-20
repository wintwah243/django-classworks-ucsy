from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import Practice2Form
from .models import Practice2


# Create your views here.

def new(request):
    if request.method == "POST":
        practice2form = Practice2Form(request.POST)

        if practice2form.is_valid():
            practice2form.save()
            return HttpResponseRedirect("/")
        else:
            practice2form = Practice2Form()

    return render(request, "practice2app/add.html", {'form': Practice2Form})


def practice2(request):
    data = Practice2.objects.all()
    return render(request, "practice2app/practice2.html", {'practice2data': data})


def update(request, id):
    data = Practice2.objects.get(id=id)

    if request.method == "POST":
        practice2form = Practice2Form(request.POST, instance=data)

        if practice2form.is_valid():
            practice2form.save()
            return HttpResponseRedirect("/")
        else:
            practice2form = Practice2Form(instance=data)

    return render(request, 'practice2app/update.html', {'form': Practice2Form})



def delete(request, id):
    Practice2.objects.get(id=id).delete()
    return HttpResponseRedirect("/")
