# Documentation de l'Application Streamlit de Prédiction des Catégories

## Introduction

L'application "Outil de prédiction des catégories" a été développée en utilisant Streamlit. L'objectif principal de cette application est d'automatiser la prédiction des catégories pour des descriptions présentes dans un fichier Excel.

## Utilisation

1. **Chargement du Fichier Excel**
   - L'utilisateur peut charger un fichier Excel en utilisant le bouton de téléchargement dédié.
   - Le fichier doit contenir au moins deux colonnes : 'Description' et 'sous ensemble '.

2. **Analyse des Données**
   - Une fois le fichier chargé, l'application analyse le nombre de lignes où la valeur dans la colonne 'sous ensemble ' est '#non catégorisé'.
   - Cette information est affichée à l'utilisateur pour une meilleure compréhension du jeu de données.

3. **Prédiction des Catégories**
   - L'utilisateur peut déclencher le processus de prédiction en cliquant sur le bouton "Effectuer une prédiction".
   - Les prédictions sont obtenues en utilisant la fonction `get_prediction` sur les descriptions du fichier Excel.
   - Les résultats, y compris la catégorie estimée et la probabilité, sont ajoutés au DataFrame d'origine.

4. **Affichage des Résultats**
   - Les résultats de la prédiction, y compris la nouvelle colonne 'sous ensemble estimé', sont affichés dans un tableau.
   - Le temps nécessaire pour effectuer les prédictions est également affiché pour donner à l'utilisateur une idée du traitement.

5. **Exportation vers Excel**
   - L'utilisateur a la possibilité de télécharger les résultats sous forme d'un fichier Excel.
   - Le fichier exporté comprend une nouvelle colonne 'sous ensemble estimé' pour faciliter la référence ultérieure.


