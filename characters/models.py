from django.db import models

class House(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=255)
    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.CharField(max_length=100)
    wand = models.CharField(max_length=255, blank=True, null=True)
    patronus = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
