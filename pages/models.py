from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    prep_time = models.IntegerField()
    ingredients = models.TextField()
    steps = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

