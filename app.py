import streamlit as st
import pandas as pd
import datetime
import requests
from myfunctions import get_prediction


def main():
    st.title("Outil de prédiction des catégories")
    st.text("Fonctionnement de l'application, le modèle utilise le contenu de la colonne \n'Description' afin de prédire le sous-ensemble. Le modèle se base sur les \nincidents déjà catégorisés par des humains pour apprendre. \nJ'ai ignoré les sous-ensembles dont le nombre d'occurences est inférieur à 10.")


    # Streamlit app code
    st.title("API Prediction App")

    # Get input from the user using st.text_input
    user_input = st.text_input("Enter text:")

    # Check if the user has entered any text
    if user_input:
        st.write(get_prediction(user_input))
        

if __name__ == "__main__":
    main()