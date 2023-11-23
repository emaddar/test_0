import streamlit as st
import pandas as pd
import datetime
import time
from myfunctions import get_prediction
from io import BytesIO
import xlsxwriter

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

        # Code de l'application Streamlit
        st.markdown(""" #### API Prediction App""")

        with st.spinner("Appel API ..."):
            # Enregistrez le temps de début
            start_time = time.time()
            result = get_prediction(text_list)
            df = pd.concat([df, result], axis=1)

            # Remplacez les valeurs de 'category' par 'à catégoriser par un humain' lorsque la 'probability' est inférieure à 0.6
            df.loc[df['probability'] < 0.6, 'category'] = 'à catégoriser par un humain'
            df = df.rename(columns={'category': 'sous ensemble estimé'})

            # Enregistrez le temps de fin
            end_time = time.time()
            
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"Temps de calcul : {round(end_time - start_time, 2)} secondes")
                st.dataframe(df)
            with col2:
                @st.cache_data
                def convert_to_csv(df):
                    # IMPORTANT: Cache the conversion to prevent computation on every rerun
                    return df.to_csv(index=False).encode('utf-8')

                csv = convert_to_csv(df)


                # download button 1 to download dataframe as csv
                download1 = st.download_button(
                    label="Download data as CSV",
                    data=csv,
                    file_name='large_df.csv',
                    mime='text/csv'
                )

                output = BytesIO()

                # Write files to in-memory strings using BytesIO
                # See: https://xlsxwriter.readthedocs.io/workbook.html?highlight=BytesIO#constructor
                workbook = xlsxwriter.Workbook(output, {'in_memory': True})
                worksheet = workbook.add_worksheet()

                worksheet.write('A1', 'Hello')
                workbook.close()

                st.download_button(
                    label="Download Excel workbook",
                    data=output.getvalue(),
                    file_name="workbook.xlsx",
                    mime="application/vnd.ms-excel"
                )
                

if __name__ == "__main__":
    main()
