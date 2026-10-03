from django.db import models

from stages.models.offre import Offre

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
    date_depot = models.DateField()
    
    offre = models.ForeignKey(
        Offre, on_delete=models.PROTECT,
        related_name="candidatures"
    )

    class Meta:
        verbose_name = "candidature"