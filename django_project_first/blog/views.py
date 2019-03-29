from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):  # don't forget to add request as argument
    # return HttpResponse('<h1>Home Page </h1>')
    return render(request, 'blog/home.html')  # .templates/blog/home.html

def about_page(request):
    return render(request, 'blog/about.html')  # .templates/blog/about.html