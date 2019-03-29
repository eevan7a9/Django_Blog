from django.shortcuts import render
from django.http import HttpResponse

dummy_post = [
    {'title': 'Hello World',
     'body': 'This is My first Post, thank you',
     'created': '2019 March-29'},
    {'title': 'Have a good day',
     'body': 'This is My second Post, thank you',
     'created': '2019 March 30'},
]


def home_page(request):  # don't forget to add request as argument
    # return HttpResponse('<h1>Home Page </h1>')
    context = {
        'posts': dummy_post,  # posts will be the key word we use on the html template
    }
    return render(request, 'blog/home.html', context)  # .templates/blog/home.html


def about_page(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})  # .templates/blog/about.html

