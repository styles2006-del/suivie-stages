from django.db import models

from stages.models.enseignant_referent import EnseignantReferent
from stages.models.tuteur_entreprise import TuteurEntreprise

class Stage(models.Model):
    sujet = models.CharField(max_length=120)
    
    tuteur_entreprise = models.ForeignKey(
            TuteurEntreprise, on_delete=models.PROTECT,
            related_name="stages"
        )
    
    enseignant_referent = models.ForeignKey(
            EnseignantReferent, on_delete=models.PROTECT,
            related_name="stages"
        )
    
    class Meta:
        verbose_name = ("stage")
        verbose_name_plural = ("stages")
        
    def __str__(self):
        return self.sujet