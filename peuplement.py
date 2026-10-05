from datetime import date
from stages.models import Competence, Entreprise, TuteurEntreprise, EnseignantReferent, Etudiant, Offre, Candidature, Stage

# --- Compétences
cpt_sql = Competence.objects.create(libelle="SQL")
cpt_js = Competence.objects.create(libelle="JavaScript")
cpt_html = Competence.objects.create(libelle="HTML/CSS")
cpt_cpp = Competence.objects.create(libelle="C++")
cpt_php = Competence.objects.create(libelle="PHP")

# --- Entreprises 
sokotech = Entreprise.objects.create(nom="SokoTech", ville="Sokodé", secteur=Entreprise.Secteur.TECHNOLOGIE, contact="a.tchalla@sokotech.tg")
agronum = Entreprise.objects.create(nom="AgroNum", ville="Sokodé", secteur=Entreprise.Secteur.COMMERCE, contact="k.mensah@agronum.tg")
lomesoft = Entreprise.objects.create(nom="LoméSoft", ville="Lomé", secteur=Entreprise.Secteur.TECHNOLOGIE, contact="p.dossou@lomesoft.tg")
sokotech = Entreprise.objects.get(nom="Sokotech")
agronum = Entreprise.objects.get(nom="AgroNum")
lomesoft = Entreprise.objects.get(nom="LoméSoft")

# --- Tuteurs 
tuteur_soko = TuteurEntreprise.objects.create(email="a.tchalla@sokotech.tg",nom="Tchalla", prenom="Abalo", sexe="M",date_naissance=date(1985, 3, 12),matricule="A123", entreprise=sokotech)
tuteur_agro = TuteurEntreprise.objects.create(email="k.mensah@agronum.tg",nom="Mensah", prenom="Kafui", sexe="F",date_naissance=date(1988, 7, 2),matricule="K456",entreprise=agronum)

# --- Enseignants référents 
ens1 = EnseignantReferent.objects.create(email="y.kpodar@ifnti.tg", nom="Kpodar", prenom="Yao", sexe="M", date_naissance=date(1978, 1, 20),matricule="Y789")
ens2 = EnseignantReferent.objects.create(email="a.agbeko@ifnti.tg",nom="Agbeko", prenom="Ama", sexe="F", date_naissance=date(1981, 9, 5),matricule="A456")


# --- Étudiants
etd1 = Etudiant.objects.create(matricule="L3-001", nom="Ayivi", prenom="Komi", sexe="M", date_naissance=date(2003, 4, 9), email="komi.ayivi@ifnti.tg", promotion=2026)
etd2 = Etudiant.objects.create(matricule="L3-002", nom="Bodjona", prenom="Akouvi", sexe="F", date_naissance=date(2002, 11, 23), email="akouvi.bodjona@ifnti.tg", promotion=2026)
etd3 = Etudiant.objects.create(matricule="L3-003", nom="Dosseh", prenom="Essi", sexe="F", date_naissance=date(2003, 6, 14), email="essi.dosseh@ifnti.tg", promotion=2026)
etd4 = Etudiant.objects.create(matricule="L3-004", nom="Eklu", prenom="Mawuli", sexe="M", date_naissance=date(2002, 2, 1), email="mawuli.eklu@ifnti.tg", promotion=2026)
etd5 = Etudiant.objects.create(matricule="L3-005", nom="Folly", prenom="Sena", sexe="F", date_naissance=date(2003, 8, 30), email="sena.folly@ifnti.tg", promotion=2026)


etd1.competences.set([cpt_sql, cpt_html])
etd2.competences.set([cpt_cpp, cpt_js])
etd3.competences.set([cpt_php, cpt_html])
etd4.competences.set([cpt_sql, cpt_js])
etd5.competences.set([cpt_cpp, cpt_php])



# --- Offres d'emploi
offre1 = Offre.objects.create(entreprise=sokotech, titre="Développeur web Django",description="Développement d'une application web interne.",
date_debut=date(2027, 2, 1), date_fin=date(2027, 7, 31), nb_places=2)

offre1.competences.set([cpt_sql, cpt_html, cpt_js])

offre2 = Offre.objects.create(entreprise=agronum, titre="Application de suivi des récoltes",description="Application Java de suivi de parcelles.",date_debut=date(2027, 2, 15), date_fin=date(2027, 8, 15), nb_places=1)

offre2.competences.set([cpt_cpp, cpt_js])

offre3 = Offre.objects.create(entreprise=lomesoft, titre="Analyste de données",description="Analyse et modélisation de données clients.",
date_debut=date(2027, 3, 1), date_fin=date(2027, 8, 31), nb_places=1)
offre3.competences.set([cpt_cpp, cpt_html])

# --- Candidatures 
S = Candidature.Statut
c1 = Candidature.objects.create(etudiant=etd1, offre=offre1, statut=S.ACCEPTER, date_depot=date(2027, 1, 10))
c2 = Candidature.objects.create(etudiant=etd2, offre=offre2, statut=S.ACCEPTER, date_depot=date(2027, 2, 15))
c3 = Candidature.objects.create(etudiant=etd3, offre=offre1, statut=S.REFUSER, date_depot=date(2027, 3, 1))
c4 = Candidature.objects.create(etudiant=etd1, offre=offre3, statut=S.ATTENTE, date_depot=date(2027, 4, 1))
c5 = Candidature.objects.create(etudiant=etd4, offre=offre2, statut=S.ATTENTE, date_depot=date(2027, 5, 1))
c6 = Candidature.objects.create(etudiant=etd5, offre=offre3, statut=S.REFUSER, date_depot=date(2027, 6, 1))

# --- Stages 
Stage.objects.create(candidature=c1,tuteur_entreprise=tuteur_soko, enseignant_referent=ens1, sujet="Gestion des stages en Django")

Stage.objects.create(candidature=c2,tuteur_entreprise=tuteur_agro, enseignant_referent=ens2, sujet="Suivi des parcelles agricoles")

o1 = Offre.objects.create(entreprise=agronum,titre="Offre incohérente",description="Fin avant le début",date_debut=date(2027, 8, 1),date_fin=date(2027, 2, 1),nb_places=1,)

o1 = Offre.objects.create(entreprise=agronum,titre="",description="Fin avant le début",date_debut=date(2027, 8, 1),date_fin=date(2027, 2, 1),nb_places=1,)
Candidature.objects.create(etudiant=etd1, offre=o1, statut=S.ATTENTE, date_depot=date(2027, 7, 1))
Candidature.objects.create(etudiant=etd1, offre=o1, statut=S.ACCEPTER, date_depot=date(2027, 7, 2))