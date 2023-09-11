from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
    
class Personal_Details(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    def __str__(self):
        return self.Name