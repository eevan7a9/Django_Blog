from django.urls import path  # to use django urls
from . import views  # to import views.py

urlpatterns = [
    path('', views.home_page, name='blog-home_page'),
    path('about/', views.about_page, name='blog-about_page'),
]
