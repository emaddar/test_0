import requests
import pandas as pd


def get_prediction(user_input):
    # Define the API endpoint
    api_endpoint = "http://20.19.222.85/predict"

    # Prepare the data in the required format
    payload = {
        "description": user_input
    }

    # Make a POST request to the API
    response = requests.post(api_endpoint, json=payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the prediction result
        result = response.json()
        #prediction = result#['category']
        return pd.DataFrame(result)#prediction
    else:
        # Return None if the request was not successful
        st.error(f"Failed to get prediction. Status code: {response.status_code}")
        return None