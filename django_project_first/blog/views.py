from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):  # don't forget to add request as argument
    return HttpResponse('<h1>Home Page </h1>')

def about_page(request):
    return HttpResponse('<h2>About Page</h2>')