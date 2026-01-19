from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Book, Category
from .forms import BookForm

# Create your views here.
def new(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)

        if book_form.is_valid():
            book_form.save()
            return HttpResponseRedirect('/')
    else:
        book_form = BookForm()

    return render(request, 'add.html', {'form': book_form})



def books(request):
    data = Book.objects.all()
    return render(request, 'books.html', {'books': data})

def update(request, id):
    data = Book.objects.get(id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=data)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
            form = BookForm(instance=data)

    return render(request, 'update.html', {'form': form})



def delete(request, id):
    Book.objects.get(id=id).delete()
    return HttpResponseRedirect('/')