from django.db import models
from django.contrib.auth.models import User
class Movie(models.Model):
    Title = models.CharField(max_length=200)
    Year = models.CharField(max_length=5,blank=True)
    Released = models.DateField(auto_now_add=True,blank=True)
    Runtime = models.CharField(max_length=10,blank=True)
    Genre = models.CharField(max_length=200,blank=True)
    Director = models.CharField(max_length=100,blank=True)
    Writer = models.CharField(max_length=100,blank=True)
    Actors =models.CharField(max_length=200,blank=True)
    Plot = models.TextField(max_length=500,blank=True)
    Language = models.CharField(max_length=100,blank=True)
    Country = models.CharField(max_length=100,blank=True)
    Awards = models.CharField(max_length=100,blank=True)
    Poster = models.ImageField(upload_to='movie/images/',blank=True)
    imdbRating = models.CharField(max_length=10,blank=True)
    imdbVotes = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.Title   
class Review(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    watchAgain = models.BooleanField()
    def __str__(self):
        return self.text