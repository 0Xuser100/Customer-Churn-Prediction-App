import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle

# Load the trained model
model = tf.keras.models.load_model('model.h5')

# Load the encoders and scaler
with open('label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open('onehot_encoder_geo.pkl', 'rb') as file:
    onehot_encoder_geo = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)


# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
    }
    .main-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #0073e6;
        margin-bottom: 30px;
    }
    .stSelectbox, .stSlider, .stNumberInput {
        background-color: #e6f2ff;
        padding: 10px;
        border-radius: 10px;
    }
    .churn-result {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        color: #0073e6;
    }
    .churn-warning {
        color: red;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.markdown('<div class="main-title">Customer Churn Prediction</div>', unsafe_allow_html=True)

# User input
geography = st.selectbox('Geography', onehot_encoder_geo.categories_[0])
gender = st.selectbox('Gender', label_encoder_gender.classes_)
age = st.slider('Age', 18, 92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])

# Prepare the input data
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

# One-hot encode 'Geography'
geo_encoded = onehot_encoder_geo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=onehot_encoder_geo.get_feature_names_out(['Geography']))

# Combine one-hot encoded columns with input data
input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

# Scale the input data
input_data_scaled = scaler.transform(input_data)

# Predict churn
prediction = model.predict(input_data_scaled)
prediction_proba = prediction[0][0]

# Display the result with custom styling
st.markdown(f'<div class="churn-result">Churn Probability: {prediction_proba:.2f}</div>', unsafe_allow_html=True)

if prediction_proba > 0.5:
    st.markdown('<div class="churn-result churn-warning">The customer is likely to churn.</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="churn-result">The customer is not likely to churn.</div>', unsafe_allow_html=True)
