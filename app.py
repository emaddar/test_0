import streamlit as st
import pandas as pd
import datetime
import time
from myfunctions import get_prediction
import io

def main():



    st.title("Outil de prédiction des catégories")
    st.text("...................................")

    # Chargez le fichier Excel
    uploaded_file = st.file_uploader("Choisissez un fichier Excel", type=['xlsx'])

    if uploaded_file is not None:
        # Lecture du fichier Excel
        df = pd.read_excel(uploaded_file).head(100)

        # Sélectionnez uniquement les colonnes 'Description', 'sous ensemble'
        selected_columns = ['Description', 'sous ensemble ']
        df = df[selected_columns]

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
                st.markdown("<h4 style='text-align: left; color: black;'>  Download data as : </h4>", unsafe_allow_html=True)
                data_type = st.radio("",("csv","xlsx"))


                if data_type == "csv":
                    data = df.to_csv(index = False).encode('utf-8')

                    st.download_button(
                    label=f"Download data as {data_type}",
                    data=data,
                    file_name=f'Data_{datetime.now()}.{data_type}',
                    mime='text/csv',
                    )

                elif data_type == "xlsx":
                        buffer = io.BytesIO()
                        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                            df.to_excel(writer, sheet_name='Data')
                            writer.save() # Close the Pandas Excel writer and output the Excel file to the buffer

                            st.download_button(
                                label=f"Download data as {data_type}",
                                data=buffer,
                                file_name=f'Data_{datetime.now()}.{data_type}',
                                mime="application/vnd.ms-excel"
                            )
                

if __name__ == "__main__":
    main()
