from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
    
class Personal_Details(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField(len=2)
    Address = models.TextField
    Pincode = models.IntegerField(max_length=6) 

    def __str__(self) -> str:
        return self.Pincode
