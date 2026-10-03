from models import Personne
from django.db import models

class Etudiant(Personne):
    matricule = models.CharField(max_length=20, unique=True)
    promotion = models.CharField(max_length=20)
    competences = models.ManyToManyField(
        'Competence', related_name='etudiants', blank=True
    )

    class Meta:
        verbose_name = ("étudiant")
        verbose_name_plural = ("étudiants")

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.matricule}"