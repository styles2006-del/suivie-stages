
from django.db import models


class Personne (models.Model):
    SEXE_CHOICES = [
            ('M', 'Masculin'),
            ('F', 'Féminin'),
        ]
    
    nom = models.CharField(max_length=120)
    prenom = models.CharField(max_length=120)
    sexe = models.CharField(
            max_length=10,
            choices=SEXE_CHOICES,
            default='M',
            verbose_name="Sexe"
    )
    date_naissance = models.DateField()
    email = models.EmailField

    

    class Meta:
        abstract = true
        verbose_name = ("personne")
        verbose_name_plural = ("personnes")

    def __str__(self):
        return self.name

    
