from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
import datetime

from django.template import loader


# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the home page.")

def about(request):
    return HttpResponse("Hello, You are at the about page.")

def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>Now time is %s.</h1></body></html>" % now
    return HttpResponse(html)

def page(request, num=1):
    html = "<html><body><h3>Number of pages: %s.</h3></body></html> " % num
    return HttpResponse(html)

def special_case_2003(request):
    return HttpResponse("this is a special case 2003")

def year_archive(request, year):
    return HttpResponse(f"Articles from {year}")

def month_archive(request, year, month):
    return HttpResponse(f"Articles from {month}/{year}")

def article_detail(request, year, month, slug):
    return HttpResponse(f"Detail page: {slug} ({month}/{year})")


def detail(request, store_id='1', location=None):
    hours = request.GET.get('hours', '')
    map = request.GET.get('map', '')

    context = {
        "store_id": store_id,
        "location": location,
        "hours": hours,
        "map": map,
    }
    return render(request, "detail.html", context)

def detailDict(request, store_id='1', location=None):
    store_name = 'Downtown'
    store_address = {'street': 'Main #385', 'city': 'San Diego', 'state': 'CA'}
    store_facility = ['Wifi', 'A/C']
    store_menu = ((0, ''), (1,'Drinks'), (2, 'Food'), (3, 'Coffee'))
    values_for_template = {'store_name': store_name, 'store_address': store_address, 'store_facility': store_facility, 'store_menu': store_menu}
    return render(request, "detailDict.html", values_for_template)


def flash_message(request):
    data = dict()
    messages.success(request, "Success: This is the sample success flash message.")
    messages.error(request, "Error: this is the sample error flash message.")
    messages.info(request, "Info: This is the sample info flash message.")
    messages.warning(request, "Warning: This is the sample warning flash message.")
    return render(request, "flashMessage.html", data)

# class MyView(View):
#     def get(self, request):
#         return render(request, "home.html")
#     def post(self, request):

def userinfo(request):
    template = loader.get_template('index_template.html')
    student = {
        'name': 'Mg Mg',
        'address': 'Yangon'
    }
    return HttpResponse(template.render(student, request))


