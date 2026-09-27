# TP — Mise en route
## Outillage

1. **uv python pin 3.14** passe la version de python à **3.14**
2. Pour que tous les étudiant aient la même version de python et aussi en cas d'erreur qu'on ait les même erreurs

## Le projet Django

1. c'est la ligne **INSTALLED_APPS = [
    'django.contrib.admin']**
2. **manage.py** permet d'exécuter les commandes django dans le projet tandis que **django-admin** est l’utilitaire en ligne de commande de Django pour les tâches administratives

## Le modèle Entreprise

### Spécification du modèle
+ La combinaison de champ qui permet d'identifier un entreprise sans ambiguïté est la combinaison de nom et de ville car dans une même ville il ne peut pas y avoir deux entreprises avec le même nom et la même ville.

+ L'adresse email est un champ de type **EmailField** et non du texte libre pour faciliter la validation et l'entrée de données.

+ Secteur d'activité une liste de choix est préférable pour éviter les erreurs de saisie et pour standardiser les données.
Le coût aujourd'hui est que je dois créer une liste de choix. Le coût dans trois mois est que si un nouveau secteur apparait je doit modifier le code pour ajouter ce nouveau secteur.

+ La derniere phrase parle de l'affichage des entreprises. Il est préférable d'afficher toutes les informations de l'entreprise.

### Migrer

1. La contrainte qui interdit les doublons est **UNIQUE**
2. C'est la colonne **id** c'est Django qui crée automatiquement cette colonne pour chaque modèle.
3. Il y a maintenant 3 fichiers. Pour revenir en arrière il faut supprimer le fichier de migration et la base de données puis recréer la base de données et refaire les migrations.

## L'administration
1. l'erreur apparait en validant.
2. oui l'erreur est compréhensible.

## La première page

1. Après avoir déplacer le template d'un dossier il y a une erreur car Django ne trouve plus le template et il nous où le template devrais se trouver.
2. Non cette page ne s'affichera pas une fois l'application en ligne. Cela dépend de **DEBUG = True** dans le fichier **settings.py**.

## Le dépôt git

1. cette chose c'est le fichier db.sqlite3 qui contient la base de données. elle ne se commit pas parce qu'il est dans le gitignore.
2. Les fichiers qui doivent se retrouver dans le dépot git sont les fichiers :
+ pyproject.toml 
+ uv.lock

Parce que ce sont les fichiers qui contiennent les dépendances du projet. Donc si quelqu'un clone le projet il pourra installer les dépendances et faire tourner le projet.