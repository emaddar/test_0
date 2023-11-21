import streamlit as st
import pandas as pd
import datetime
import requests



def main():
    st.title("Outil de prédiction des catégories")
    st.text("Fonctionnement de l'application, le modèle utilise le contenu de la colonne \n'Description' afin de prédire le sous-ensemble. Le modèle se base sur les \nincidents déjà catégorisés par des humains pour apprendre. \nJ'ai ignoré les sous-ensembles dont le nombre d'occurences est inférieur à 10.")


    # Streamlit app code
    st.title("API Prediction App")

    # Get input from the user using st.text_input
    user_input = st.text_input("Enter text:")

    # Check if the user has entered any text
    if user_input:
        # Define the API endpoint
        api_endpoint = "http://20.19.222.85/predict"

        # Prepare the data in the required format
        payload = {
            "description": [user_input]
        }

        # Make a POST request to the API
        response = requests.post(api_endpoint, json=payload)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Display the prediction result
            result = response.json()
            st.success(f"Prediction: {result['prediction'][0]}")
        else:
            # Display an error message if the request was not successful
            st.error(f"Failed to get prediction. Status code: {response.status_code}")

if __name__ == "__main__":
    main()