import streamlit as st
import pickle
import numpy as np

# Set background image
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://api.time.com/wp-content/uploads/2016/05/relationship-dealbreaker.jpg?quality=85&w=4577") no-repeat center center fixed;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Load the trained model
model = pickle.load(open('Heart_failure.pkl', 'rb'))

# Function to predict heart failure
def predict_heart_failure(age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope):
    # Preprocess the input features
    features = [age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope]
    
    # Perform any required preprocessing or feature engineering
    
    # Make predictions
    prediction = model.predict([features])[0]
    
    return prediction

# Create the web app using Streamlit
def main():
    # Set the title and description
    st.title("Heart Failure Prediction")
    st.write("This web app predicts the likelihood of heart failure based on input features.")
    
    # Create input fields for user input
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    sex = st.selectbox("Sex", ["Male", "Female"])
    chest_pain_type = st.selectbox("Chest Pain Type", ["ASY", "NAP", "ATA", "TA"])
    resting_bp = st.number_input("Resting Blood Pressure", min_value=1, max_value=300, step=1)
    cholesterol = st.number_input("Cholesterol", min_value=1, max_value=1000, step=1)
    fasting_bs = st.selectbox("Fasting Blood Sugar", ["False", "True"])
    resting_ecg = st.selectbox("Resting ECG", ["Normal", "LVH", "ST"])
    max_hr = st.number_input("Max Heart Rate", min_value=1, max_value=300, step=1)
    exercise_angina = st.selectbox("Exercise-Induced Angina", ["No", "Yes"])
    oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, step=0.1)
    st_slope = st.selectbox("ST Slope", ["Upsloping", "Flat", "Downsloping"])
    
    # Predict heart failure on button click
    if st.button("Predict"):
        sex = 1 if sex == "Male" else 0
        fasting_bs = 1 if fasting_bs == "True" else 0
        exercise_angina = 1 if exercise_angina == "Yes" else 0
        
        prediction = predict_heart_failure(age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope)
        
        if prediction == 0:
            st.write("The likelihood of heart failure is low.")
        else:
            st.write("The likelihood of heart failure is high.")

# Run the web app
if __name__ == '__main__':
    main()
