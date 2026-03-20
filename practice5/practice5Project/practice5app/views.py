from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import Practice5Form
from .models import Practice5


# Create your views here.
def new(request):
    if request.method == "POST":
        practice5form = Practice5Form(request.POST)

        if practice5form.is_valid():
            practice5form.save()
            return HttpResponseRedirect("/")
        else:
            practice5form = Practice5Form()

    return render(request, "practice5app/add.html", {"form": Practice5Form})


def practice5(request):
    data = Practice5.objects.all()
    return render(request, "practice5app/practice5.html", {"practice5data": data})

def update(request, id):
    data = Practice5.objects.get(id=id)

    if request.method == "POST":
        form = Practice5Form(request.POST, instance=data)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            form = Practice5Form(instance=data)

    return render(request, "practice5app/update.html", {"form": Practice5Form})

def delete(request, id):
    Practice5.objects.get(id=id).delete()
    return HttpResponseRedirect("/")