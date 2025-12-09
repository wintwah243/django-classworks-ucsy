from django.shortcuts import render
from django.http import HttpResponse
import datetime

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
