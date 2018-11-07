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
    entreprises_impactés = models.CharField(max_length=40, default="")
    creation_date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de création")
    class Meta:
        verbose_name = "litige"
        ordering = ['creation_date']

    def __str__(self):
        return self.entreprises_impactés