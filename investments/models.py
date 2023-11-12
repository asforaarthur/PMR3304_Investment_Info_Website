from django.db import models
from django.conf import settings


class Investment(models.Model):
    name = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    image_url = models.URLField(max_length=200, null=True)
    texto = models.CharField(max_length=3000, null=True)
    def __str__(self):
        return f"{self.name}"


class Comentario(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'

class List(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    investments = models.ManyToManyField(Investment)

    def __str__(self):
        return f"{self.name} by {self.author}"
