from django.db import models
from django.db.models import CharField, ForeignKey, ImageField
from django.conf import settings
from django.utils import timezone


class HiddenVillages(models.Model):
    name = CharField(max_length=30)
    symbol = ImageField()

    def __str__(self):
        return self.name


class Nija(models.Model):
    SEX = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    gender = CharField(max_length=1, choices=SEX)
    village = ForeignKey(HiddenVillages,
                         related_name='village',
                         on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class NijaImage(models.Model):
    nija = ForeignKey(Nija,
                      on_delete=models.CASCADE,
                      related_name='images')
    image = models.ImageField()

    def __str__(self):
        return self.image.url
