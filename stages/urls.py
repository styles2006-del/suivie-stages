from django.urls import path
from . import views

app_name = "stages"
urlpatterns = [
    path("entreprises/", views.liste_entreprises, name="liste_entreprises"),
    path("offres/", views.liste_offres, name="listes_offres"),
    path("offres/<int:id>",views.details_offre, name="details_offre")
]
