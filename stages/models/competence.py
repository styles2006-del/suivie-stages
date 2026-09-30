from django.db import models

class Competence(models.Model):
    libelle = models.CharField(max_length=120)