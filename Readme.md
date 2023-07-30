Dans ce projet, nous avons pour objectif de créer des modèles d'apprentissage automatique (Machine Learning) pour le Traitement Automatique du Langage Naturel (NLP) afin de catégoriser automatiquement les questions posées sur le forum de Stack Overflow.

Les étapes à réaliser sont les suivantes :

Filtrage des données : Nous allons extraire et filtrer les données pertinentes à partir de l'API Stack Exchange Explorer.

Prétraitement des documents : Les données textuelles des questions seront prétraitées pour les rendre exploitables par les modèles NLP, notamment en effectuant des opérations de tokenization, de suppression des mots vides (stop words) et de lemmatisation.

Approches supervisées et non supervisées : Nous allons comparer différentes approches pour prédire les tags des questions. Du côté supervisé, nous utiliserons les algorithmes de Régression Logistique et Random Forest pour classifier les questions avec leurs tags correspondants. Du côté non supervisé, nous explorerons les techniques de Latent Dirichlet Allocation (LDA) et Non-Negative Matrix Factorization (NMF) pour regrouper les questions en sujets thématiques.

Implémentation de l'API : Nous créerons des fonctions et des classes nécessaires pour l'implémentation de l'API de suggestion de tags. Cette API sera capable de prendre en entrée une question et de renvoyer les tags les plus pertinents pour celle-ci.

Développement et mise en production de l'API : Une fois l'API développée, nous la mettrons en production pour qu'elle puisse être utilisée par les utilisateurs de Stack Overflow, en particulier pour aider les débutants en leur suggérant des tags pertinents pour leurs questions ou interrogations.

En résumé, ce projet vise à créer une API de suggestion de tags pour Stack Overflow en utilisant des techniques d'apprentissage automatique en NLP, tant supervisées que non supervisées, pour améliorer la catégorisation automatique des questions posées sur la plateforme.





