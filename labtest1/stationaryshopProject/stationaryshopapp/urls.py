from django.urls import path
from . import views

urlpatterns = [
    path('', views.stationary, name='books'),
    path('new/', views.new, name='new'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
]