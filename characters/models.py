from django.db import models

class House(models.Model):
    name = models.CharField(max_length=100)

class Character(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('professor', 'Professor'),
        ('auror', 'Auror'),
        ('minister', 'Minister'),
    ]

    PATRONUS_CHOICES = [
    ('stag', 'Stag'),
    ('otter', 'Otter'),
    ('phoenix', 'Phoenix'),
    ('wolf', 'Wolf'),
    ]

    WAND_CHOICES = [
    ('holly_phoenix', 'Holly, Phoenix Feather'),
    ('elm_dragon', 'Elm, Dragon Heartstring'),
    ]

    wand = models.CharField(max_length=100, choices=WAND_CHOICES, blank=True, null=True)
    patronus = models.CharField(max_length=100, choices=PATRONUS_CHOICES, blank=True, null=True)



class Character(models.Model):
    name = models.CharField(max_length=255)
    house = models.ForeignKey('House', on_delete=models.CASCADE)
    role = models.CharField(max_length=255, null=True, blank=True)
    wand = models.CharField(max_length=255, null=True, blank=True)
    patronus = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name