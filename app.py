import streamlit as st
import pandas as pd
import datetime
from myfunctions import get_prediction


def main():
    st.title("Outil de prédiction des catégories")
    st.text("...................................")

    
    uploaded_file = st.file_uploader("Choisissez un fichier Excel", type=['xlsx'])
    
    
    if uploaded_file is not None:
        first = st.number_input('first N rows : ')
        if first :
            # Lecture du fichier Excel
            df = pd.read_excel(uploaded_file).head(first)
            # Select only the columns 'Description', 'sous ensemble'
            selected_columns = ['Description', 'sous ensemble ']
            df = df[selected_columns]

            # Select only the rows where 'sous ensemble ' is "#non catégorisé"
            df_filtered = df[df['sous ensemble '] == "#non catégorisé"]

            # Print the number of rows
            st.write("Nombre de lignes avec 'sous ensemble' en tant que '#non catégorisé':", len(df_filtered))

            text_list = df_filtered['Description'].values.tolist()
        

            # Streamlit app code
            st.title("API Prediction App")

        

            with st.spinner("call api ..."):
                st.write(get_prediction(text_list))
        

if __name__ == "__main__":
    main()
    





    #     model = load_model('nlp_14_nb_class_2023-11-21 11 24 44.996424.h5')  

    #     predictions = make_predictions(model, df)
        
        
        # df['Prédictions'] = predictions  # Ajouter les prédictions au dataframe

        # # Sauvegarder le dataframe modifié en tant que nouveau fichier Excel
        # output_file = 'predictions.xlsx'
        # df.to_excel(output_file, index=False)

        # # Permettre le téléchargement du nouveau fichier
        # st.download_button(
        #     label="Télécharger le fichier Excel avec prédictions",
        #     data=output_file,
        #     file_name=output_file,
        #     mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        # )

    # col1, col2, col3 , col4, col5= st.columns(5)

    # with col1 :

    #     st.markdown("<h4 style='text-align: left; color: black;'>  Download data as : </h4>", unsafe_allow_html=True)
    #     data_type = st.radio("",("csv","xlsx"))


    #     if data_type == "csv":
    #         data = df.to_csv(index = False).encode('utf-8')

    #         st.download_button(
    #         label=f"Download data as {data_type}",
    #         data=data,
    #         file_name=f'Data_{datetime.now()}.{data_type}',
    #         mime='text/csv',
    #         )

    #     elif data_type == "xlsx":
    #             buffer = io.BytesIO()
    #             with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
    #                 df.to_excel(writer, sheet_name='Data')
    #                 writer.save() # Close the Pandas Excel writer and output the Excel file to the buffer

    #                 st.download_button(
    #                     label=f"Download data as {data_type}",
    #                     data=buffer,
    #                     file_name=f'Data_{datetime.now()}.{data_type}',
    #                     mime="application/vnd.ms-excel"
    #                 )
    
