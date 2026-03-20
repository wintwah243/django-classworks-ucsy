from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import Practice1Form
from .models import Practice1


def new(request):
    if request.method == 'POST':
        practice1form = Practice1Form(request.POST)

        if practice1form.is_valid():
            practice1form.save()
            return HttpResponseRedirect('/')
        else:
            practice1form = Practice1Form()

    return render(request, 'practice1app/add.html', {'form': Practice1Form})


def practice1(request):
    data = Practice1.objects.all()
    return render(request, 'practice1app/practice1.html', {'practice1data': data})


def update(request, id):
    data = Practice1.objects.get(id=id)

    if request.method == 'POST':
        form = Practice1Form(request.POST, instance=data)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            form = Practice1Form(instance=data)

    return render(request, 'practice1app/update.html', {'form': Practice1Form})


def delete(request, id):
    Practice1.objects.get(id=id).delete()
    return HttpResponseRedirect('/')