from django.contrib import admin
from .models import Post  #to be able to access the posts

admin.site.register(Post)
# Register your models here.
