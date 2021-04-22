from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200 )
	content = models.TextField()
	author = models.ForeignKey(User, on_delete= models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk' : self.pk})

	@property
	def comment(self):
		return self.comment_set.all()

class Comment(models.Model):
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk' : self.post.pk})
		