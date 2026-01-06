from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('list/', views.list_view, name='list'),
]
