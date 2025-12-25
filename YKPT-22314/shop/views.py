from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, 'shop/home.html')

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == 'POST':
        request.session['coffee'] = request.POST.get('coffee')
        request.session['qty'] = request.POST.get('qty')
        messages.success(request, 'Order placed successfully!')
        return redirect('order')
    return render(request, 'shop/contact.html')

def order(request):
    context = {
        'coffee': request.session.get('coffee'),
        'qty': request.session.get('qty'),
    }
    return render(request, 'shop/order.html', context)
