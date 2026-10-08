from django.shortcuts import render
from stages.models.offre import Offre

def liste_offres(request):
    offres = (Offre.objects.prefetch_related("competences").select_related("entreprise"))
    return render(
        request,
        "stages/listes_offres.html",
        {"offres":offres}
    )

def details_offre(request,id):
    offre = Offre.objects.get(id=id)
    return render(
        request,
        "stages/details_offre.html",
        {"offre":offre}
    )

