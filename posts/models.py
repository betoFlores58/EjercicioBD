from django.db import models

# Create your models here.

class Post(models.Model):
    text=models.TextField()
    title=models.TextField(default="")
    img = models.TextField(default="")

    def __str__(self):
        return self.text[:50]

class Texto(models.Model):
    parrafo = models.TextField()
    title=models.TextField(default="")
    autor=models.TextField(default="")

    def __str__(self):
        return self.parrafo[:50000]
