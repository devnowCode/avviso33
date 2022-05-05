from django.db import models

class Lezioni(models.Model):
    titolo = models.CharField(max_length=80)
    nota = models.CharField(max_length=255)
    link = models.CharField(max_length=2083)