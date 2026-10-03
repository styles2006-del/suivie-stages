from django.db import models

from stages.models.personne import Personne
from stages.models.entreprise import Entreprise
from stages.models.stage import Stage

class TuteurEntreprise(Personne):
    matricule = models.CharField(max_length=120)

    entreprise = models.ForeignKey(
        Entreprise, on_delete=models.PROTECT,
        related_name="tuteur_entreprises"
    )
    
    class Meta(Personne.Meta):
        verbose_name = "tuteur_entreprise"