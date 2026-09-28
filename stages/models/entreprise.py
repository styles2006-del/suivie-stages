from django.db import models
from django.db.models import UniqueConstraint

# Create your models here.

class Entreprise(models.Model):
    """Une entreprise susceptible d'acceuillir un stagiaire"""
    class Secteur(models.TextChoices):
        TECHNOLOGIE = "technologie"
        COMMERCE = "commerce"
        SANTE = "sante"
        FINANCE = "finance"
        INDUSTRIE = "industrie"
        AUTRE = "autre"
        

    nom = models.CharField(max_length=120, unique=True)
    ville = models.CharField(max_length=80)
    secteur = models.CharField(
        max_length=80, 
        choices=Secteur.choices,
        default=Secteur.AUTRE
        )
    contact = models.EmailField()

    class Meta:
        ordering = ["nom"]
        verbose_name = "entreprise"
        verbose_name_plural = "entreprises"
        constraints = [
            UniqueConstraint(fields=["nom", "ville"], name="nom_ville_unique")
        ]

    def __str__(self):
        return f"{self.nom} - ({self.ville}) - {self.secteur} - {self.contact}"
    