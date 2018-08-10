from django.db import models

# Create your models here.

from django.conf import settings

User = settings.AUTH_USER_MODEL


class Post(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	author = models.ForeignKey('Author')
	image = models.ImageField()
	slug = models.SlugField(unique=True) #posts/1/ --> /posts/first/

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/posts/{}/".format(self.slug)

	def get_update_url(self):
		return "/posts/{}/update/".format(self.slug)

	def get_delete_url(self):
		return "/posts/{}/delete/".format(self.slug)


class Author(models.Model):
	user = models.ForeignKey(User)
	email = models.EmailField()
	cellphone_num = models.IntegerField()# "+27"

	def __str__(self):
		return self.user.username