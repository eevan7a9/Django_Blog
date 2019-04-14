from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home_page(request):  # don't forget to add request as argument
    # return HttpResponse('<h1>Home Page </h1>')
    context = {
        'posts': Post.objects.all(),  # posts will be the key word we use on the html template
    }
    # return render(request, 'blog/home.html.django', context)  # .templates/blog/home.html
    return render(request, 'blog/home.html', context)

def about_page(request):
    return render(request, 'blog/about.html')  # .templates/blog/about.html
