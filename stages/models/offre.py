from django.db import models

from stages.models.entreprise import Entreprise

class Offre(models.Model):
    titre = models.CharField(max_length=120)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    nb_places = models.IntegerField()
    
    entreprise = models.ForeignKey(
        Entreprise, on_delete=models.PROTECT,
        related_name="offres"
    )
    
    competences = models.ManyToManyField(
        "Competence", related_name="offres"
    )
    
    class Meta:
        verbose_name = "offre"
        verbose_name_plural = "offres"