from django.db import models

from stages.models.personne import Personne

class EnseignantReferent(Personne):
    matricule = models.CharField(max_length=120)
    
    class Meta:
        verbose_name = "enseignant référent"
        verbose_name_plural = "enseignants référents"