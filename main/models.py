from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	cDate = models.DateTimeField(default=timezone.now)
	pDate = models.DateTimeField(blank=True,null=True)
	
	def publish(self):
		self.pData = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title
