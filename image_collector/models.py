from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content  = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)

class Images(models.Model): 
    name = models.CharField(max_length=50) 
    class_img = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name