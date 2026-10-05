# Requêtes Django ORM

from stages.models import *
etu = Etudiant.objects.get(matricule="L3-001")
Offre.objects.filter(entreprise__ville="Sokodé")
Etudiant.objects.filter(competences__libelle="Django")
etu.candidatures.all()
Candidature.objects.filter(statut=Candidature.Statut.ACCEPTER).count()
Stage.objects.filter(candidature__offre__entreprise__ville="Sokodé")
Offre.objects.filter(competences__in=etu.competences.all())
** Cette requête renvoie des doublons pour corriger il faut ajouter un distinct() **
Offre.objects.filter(competences__in=etu.competences.all()).distinct()