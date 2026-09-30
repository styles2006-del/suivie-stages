from django.db import models

class Candidature(models.Model):
    class Statut(models.TextChoices):
        ACCEPTER = "accepter"
        REFUSER = "refuser"
        ATTENTE = "en attente"

    statut = models.CharField(
        max_length=80,
        choices=Statut.choices,
        default=Statut.ATTENTE
    )