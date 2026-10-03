from django.db import models

class Stage(models.Model):
    sujet = models.CharField(max_length=120)
    
    class Meta:
        verbose_name = ("stage")
        verbose_name_plural = ("stages")
        
    def __str__(self):
        return self.nom