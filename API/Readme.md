Ce projet a pour objectif de créer une API de suggestion de tags en utilisant des modèles d'apprentissage automatique supervisés et non supervisés, afin de faciliter la catégorisation automatique des questions posées sur Stack Overflow.

Le contenu du repository est organisé comme suit :

- Dossier "Model" : Contient les modèles utilisés pour concevoir l'API. Ces modèles peuvent inclure des approches supervisées (Regression logistique, Random Forest) et non supervisées (LDA, NMF) pour prédire les tags des questions.

- Dossier "Template" : Contient le code HTML et CSS pour créer l'interface de l'API. Cette interface permettra aux utilisateurs de poser des questions et d'obtenir des suggestions de tags pertinents.

- Fichier "app.py" : Regroupe l'ensemble des fonctions nécessaires pour exécuter l'API, ainsi que l'API elle-même. Ce fichier joue le rôle de serveur et prend en charge les requêtes des utilisateurs.
- Fichier module.py contenant l'ensemble des fonctions de prétraitement des données et de prédiction des tags.

- Fichier "requirements" : Liste l'ensemble des packages et dépendances utilisés dans le projet, ce qui permet de reproduire facilement l'environnement d'exécution de l'API.

- Fichier "runtime" : Indique la version de Python utilisée pour développer et exécuter l'API, ce qui permet d'assurer la compatibilité et la reproductibilité du projet.
