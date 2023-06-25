import pickle
import streamlit as st
import numpy as np

# Load the trained model
model = pickle.load(open('Heart_failure.pkl', 'rb'))

# Function to preprocess input features
def preprocess_features(age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope):
    # Encode categorical features
    sex_encoded = 1 if sex == "Male" else 0
    fasting_bs_encoded = 1 if fasting_bs == "True" else 0
    exercise_angina_encoded = 1 if exercise_angina == "Yes" else 0

    # Convert categorical features to numerical values
    chest_pain_mapping = {"ASY": 0, "NAP": 1, "ATA": 2, "TA": 3}
    resting_ecg_mapping = {"Normal": 0, "LVH": 1, "ST": 2}
    st_slope_mapping = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}

    chest_pain_type_encoded = chest_pain_mapping.get(chest_pain_type, -1)
    resting_ecg_encoded = resting_ecg_mapping.get(resting_ecg, -1)
    st_slope_encoded = st_slope_mapping.get(st_slope, -1)

    # Create a feature vector
    features = [age, sex_encoded, chest_pain_type_encoded, resting_bp, cholesterol, fasting_bs_encoded, resting_ecg_encoded, max_hr, exercise_angina_encoded, oldpeak, st_slope_encoded]

    return features

# Function to predict heart failure
def predict_heart_failure(features):
    # Perform any required preprocessing or feature engineering

    # Convert the feature list to a NumPy array
    features_array = np.array(features).reshape(1, -1)

    # Make predictions
    prediction = model.predict(features_array)[0]

    return prediction

# Create the web app using Streamlit
def main():
    st.markdown(
        """
        <style>
        .reportview-container {
            background: url('https://api.time.com/wp-content/uploads/2016/05/relationship-dealbreaker.jpg?quality=85&w=4577') no-repeat center center fixed;
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
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
        features = preprocess_features(age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope)
        prediction = predict_heart_failure(features)

        if prediction == 0:
            st.write("The likelihood of heart failure is low.")
        else:
            st.write("The likelihood of heart failure is high.")

# Run the web app
if __name__ == '__main__':
    main()
