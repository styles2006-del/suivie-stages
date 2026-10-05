# TP — Modéliser le domaine
## 1. Un Modèle par fichier
**a.** Django me dit **no changes detected**. Django identifie un modèle par le nom de la classe et non par le nom du fichier. Une migration c'est la manière dont django propages le modifications apportés à des modèle sur une base de données.


## 6. Ce que la base accepte

6.a. Les deux premieres requête sont acceptées par la base de données. La troisième requête n'est pas acceptée par la base de données.

6.b. les premières et deuxièmes requêtes relèvent du même problème car les information ne sont pas valider par le formulaire avant d'être soumis à la base de données. Selon moi la base aurait du refuser ces données.