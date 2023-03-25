from django.db import models

# Create your models here.
class HomeSlider(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='slider')
    headline = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=50, null=True, blank=True)
    
    
class HomeSlider2(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='slider')
    date = models.DateTimeField(auto_created=True)
    title = models.TextField(max_length=100, null=True, blank=True)