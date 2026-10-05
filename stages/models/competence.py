from django.db import models

class Competence(models.Model):
    libelle = models.CharField(max_length=120)
    
    
    class Meta:
        verbose_name = ("compétence")
        verbose_name_plural = ("compétences")
        
    
        
    def __str__(self):
        return self.libelle