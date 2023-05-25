from django.db import models
from django.contrib.auth.models import User

class truyen (models.Model):
    img = models.ImageField(upload_to='truyen/')
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    description = models.TextField(null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return self.title
    
class chapter (models.Model):
    truyen = models.ForeignKey(truyen, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    


class category (models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    def __str__(self):
        return self.title
    
class truyen_category (models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    truyen = models.ForeignKey(truyen, on_delete= models.CASCADE)