from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone

# Create your models here.

class Litige(models.Model):
    fai = models.ForeignKey(User, on_delete=models.CASCADE)  # La liaison OneToOne vers le modèle User
    tempsdown = models.CharField(max_length=40)
    compensation = models.CharField(max_length=40)
    cause = models.CharField(max_length=400)
    entreprises_impactées = models.CharField(max_length=40, default="")
    creation_date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de création")
    class Meta:
        verbose_name = "litige"
        ordering = ['creation_date']

    def __str__(self):
        return self.entreprises_impactées

class Client(models.Model):
    id_client = models.IntegerField(default=0)
    name = models.CharField(max_length=30)
    adresse = models.CharField(max_length=90)

    class Meta:
        verbose_name = "client"
        ordering = ['id_client']

    def __str__ (self):
        return self.name