from django.urls import path
from . import views

urlpatterns = [
    path('', views.practice3, name='practice3'),
    path('new/', views.new, name='new'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]