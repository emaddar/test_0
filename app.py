import streamlit as st
import pandas as pd
import datetime
from myfunctions import get_prediction
import time

def main():

    # Enregistrez le temps de début
    start_time = time.time()

    st.title("Outil de prédiction des catégories")
    st.text("...................................")

    # Chargez le fichier Excel
    uploaded_file = st.file_uploader("Choisissez un fichier Excel", type=['xlsx'])

    if uploaded_file is not None:
        # Lecture du fichier Excel
        df = pd.read_excel(uploaded_file)

        # Sélectionnez uniquement les colonnes 'Description', 'sous ensemble'
        selected_columns = ['Description', 'sous ensemble ']
        df = df[selected_columns]

        # Sélectionnez uniquement les lignes où 'sous ensemble ' est "#non catégorisé"
        df_filtered = df[df['sous ensemble '] == "#non catégorisé"]

        # Affichez le nombre de lignes
        st.write("Nombre de lignes avec 'sous ensemble' en tant que '#non catégorisé':", len(df_filtered))

        text_list = df_filtered['Description'].values.tolist()

        # Code de l'application Streamlit
        st.title("API Prediction App")

        with st.spinner("Appel API ..."):
            result = get_prediction(text_list)
            df = pd.concat([df, result], axis=1)

            # Remplacez les valeurs de 'category' par 'à catégoriser par un humain' lorsque la 'probability' est inférieure à 0.6
            df.loc[df['probability'] < 0.6, 'category'] = 'à catégoriser par un humain'
            df = df.rename(columns={'category': 'sous ensemble estimé'})
            st.dataframe(df)

            # Enregistrez le temps de fin
            end_time = time.time()
            st.write(f"Temps de calcul : {end_time - start_time} secondes")

if __name__ == "__main__":
    main()
