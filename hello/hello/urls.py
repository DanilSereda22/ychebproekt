from django.contrib import admin
from django.urls import path
from django.urls import re_path
from firstapp import views
from django.views.generic import TemplateView

urlpatterns = [
 path('', views.index),
 path('about/', TemplateView.as_view(template_name="firstapp/about.html")),
 path('contact/', TemplateView.as_view(template_name="firstapp/contact.html")),
 path('details/', views.details),
 path('products/', views.products),
 path('products/<int:productid>/', views.products),
 path('users/', views.users), 
 path('users/<int:id>/<str:name>/', views.users),
]