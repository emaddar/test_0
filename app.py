import streamlit as st
import pandas as pd
import datetime
import time
from myfunctions import get_prediction, to_excel
from io import BytesIO
import xlsxwriter


st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide")




def main():



    st.title("Outil de prédiction des catégories")
    st.text("...................................")

    # Chargez le fichier Excel
    uploaded_file = st.file_uploader("Choisissez un fichier Excel", type=['xlsx'])

    if uploaded_file is not None:
        # Lecture du fichier Excel
        df = pd.read_excel(uploaded_file)

        # Sélectionnez uniquement les colonnes 'Description', 'sous ensemble'
        selected_columns = ['Description', 'sous ensemble ']
        df = df[selected_columns].head(100)

        # Sélectionnez uniquement les lignes où 'sous ensemble ' est "#non catégorisé"
        # df_filtered = df[df['sous ensemble '] == "#non catégorisé"]

        # Affichez le nombre de lignes
        st.write("Nombre de lignes avec 'sous ensemble' en tant que '#non catégorisé':", len(df))

        text_list = df['Description'].values.tolist()

        st.markdown("----", unsafe_allow_html=True)
        columns = st.columns((2, 1, 2))
        button = columns[1].button('Effectuer une prédiction')
        st.markdown("----", unsafe_allow_html=True)


        col1, col2 = st.columns(2)
        

        
        with col1:

                if button :

                    # Code de l'application Streamlit
                    st.markdown(""" #### API Prediction App""")

                    with st.spinner("Appel API ..."):
                        # Enregistrez le temps de début
                        start_time = time.time()
                        result = get_prediction(text_list)
                        df = pd.concat([df, result], axis=1)

                        # Remplacez les valeurs de 'category' par 'à catégoriser par un humain' lorsque la 'probability' est inférieure à 0.6
                        df.loc[df['probability'] < 0.6, 'category'] = 'à catégoriser par un humain'
                        df_pred = df.rename(columns={'category': 'sous ensemble estimé'})

                        # Enregistrez le temps de fin
                        end_time = time.time()
                
                
            
                        st.write(f"Temps de calcul : {round(end_time - start_time, 2)} secondes")
                        st.dataframe(df_pred)



        if df_pred  is not null:
            with col23:          
                    df_xlsx = to_excel(df_pred)   
                    st.download_button(label='📥 Download Current Result',
                                                    data=df_xlsx ,
                                                    file_name= 'df_test.xlsx')
                        

                

if __name__ == "__main__":
    main()
