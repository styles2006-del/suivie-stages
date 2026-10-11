from django.shortcuts import get_object_or_404, render

from stages.models.entreprise import Entreprise
from stages.models.offre import Offre

def liste_entreprises(request):
    return render(
        request,
        'stages/liste_entreprises.html',
        { "entreprises" : Entreprise.objects.all()}
    )

def detail_entreprise(request,id):
    entreprise = get_object_or_404(Entreprise, id=id)
    offres = Offre.objects.filter(entreprise_id=id)
    return render(
        request,
        "stages/detail_entreprise.html",
        {
            "entreprise" : entreprise,
            "offres" : offres
        }
    )