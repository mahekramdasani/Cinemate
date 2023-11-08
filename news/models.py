from django.db import models
from datetime import date
# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length=100)
    description = models.TextField(max_length=250,blank=True)
    date = models.DateField(default=date.today,blank=True)
    url = models.URLField(blank=True)
    urlToImage = models.ImageField(upload_to='news/images/',blank=True)
    def __str__(self):
        return self.headline