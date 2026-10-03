from django.db import models

from stages.models.personne import Personne
from stages.models.stage import Stage

class EnseignantReferent(Personne):
    matricule = models.CharField(max_length=120)
    
    stage = models.ForeignKey(
        Stage, on_delete=models.PROTECT,
        related_name="enseignant_referents"
    )
    class Meta:
        verbose_name = "enseignant référent"
        verbose_name_plural = "enseignants référents"