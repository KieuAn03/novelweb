from django.db import models
from django.contrib.auth.models import User

class truyen (models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='truyen/')
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    description = models.TextField(null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(null=True, default=0)
    def __str__ (self):
        return self.title
    
class chapter (models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='chapter/', null= True)
    truyen = models.ForeignKey(truyen, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.truyen.title + " : " + self.title
    

class category (models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    def __str__(self):
        return self.title
    
class truyen_category (models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    Truyen = models.ForeignKey(truyen, on_delete= models.CASCADE)
    def __str__(self):
        return self.Truyen.title + " : " + self.category.title

class favorate (models.Model):
    id = models.AutoField(primary_key=True)
    truyen = models.ForeignKey(truyen, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.truyen.title + " : " + self.user.username
class comment (models.Model):
    id = models.AutoField(primary_key=True)
    truyen = models.ForeignKey(truyen, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    date_published = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username + " : " + self.truyen.title +" : "+ self.content[:10] + "..."
    
   