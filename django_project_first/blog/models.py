from django.db import models
from django.utils import timezone  # we need this coz we use timezone for 'created_at'
from django.contrib.auth.models import User  # we need this to be able to set user as primary key
# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
