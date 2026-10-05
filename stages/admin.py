from django.contrib import admin
from .models import Entreprise
from .models import TuteurEntreprise
from .models import EnseignantReferent
from .models import Candidature
from .models import Stage
from .models import Offre
from .models import Competence
from .models import Etudiant

# Register your models here.

@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ["nom","ville","secteur"]
    search_fields = ["nom","ville"]
    

    
    
@admin.register(TuteurEntreprise)
class TuteurEntrepriseAdmin(admin.ModelAdmin):
    list_display = ["nom","prenom","email","matricule","entreprise"]
    search_fields = ["nom","prenom","email","matricule"]
    
    
@admin.register(EnseignantReferent)
class EnseignantReferentAdmin(admin.ModelAdmin):
    list_display = ["nom","prenom","email","matricule"]
    search_fields = ["nom","prenom","email","matricule"]
    
    
@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    list_display = ["etudiant","offre","date_depot","statut"]
    search_fields = ["etudiant__nom","etudiant__prenom","offre__titre"]
    
@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ["sujet","tuteur_entreprise","enseignant_referent","candidature"]
    search_fields = ["sujet","tuteur_entreprise__nom","enseignant_referent__nom","candidature__etudiant__nom"]
    
@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display = ["titre","description","entreprise","date_debut","date_fin","nb_places"]
    search_fields = ["titre","entreprise__nom"]
    
@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ["libelle"]
    search_fields = ["libelle"]
    
@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ["nom","prenom","email","matricule","promotion"]
    search_fields = ["nom","prenom","email","matricule"]
    

