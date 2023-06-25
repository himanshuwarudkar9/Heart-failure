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
    st.markdown("<h1 style='color: #333; font-weight: bold;'>Heart Failure Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #333; font-weight: bold;'>This web app predicts the likelihood of heart failure based on input features.</p>", unsafe_allow_html=True)
    
    st.sidebar.subheader("Disclaimer")
    st.sidebar.write("This prediction model is for informational purposes only. The results provided should not be considered as medical advice or a definitive diagnosis. Please consult with a qualified healthcare professional for an accurate evaluation of your heart health.")
    # Create input fields for user input
    age = st.number_input("Age", min_value=1, max_value=120, step=1, help="Enter the age in years.")
    sex = st.radio("Sex", ["Male", "Female"], help="Select the gender.")
    chest_pain_type = st.selectbox("Chest Pain Type", ["ASY", "NAP", "ATA", "TA"], help="Select the type of chest pain.")
    resting_bp = st.number_input("Resting Blood Pressure", min_value=1, max_value=300, step=1, help="Enter the resting blood pressure in mmHg.")
    cholesterol = st.number_input("Cholesterol", min_value=1, max_value=1000, step=1, help="Enter the cholesterol level in mg/dL.")
    fasting_bs = st.selectbox("Fasting Blood Sugar", ["False", "True"], help="Select the fasting blood sugar level.")
    resting_ecg = st.selectbox("Resting ECG", ["Normal", "LVH", "ST"], help="Select the resting electrocardiographic results.")
    max_hr = st.number_input("Max Heart Rate", min_value=1, max_value=300, step=1, help="Enter the maximum heart rate achieved.")
    exercise_angina = st.selectbox("Exercise-Induced Angina", ["No", "Yes"], help="Select whether exercise-induced angina is present.")
    oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, step=0.1, help="Enter the ST depression induced by exercise relative to rest.")
    st_slope = st.selectbox("ST Slope", ["Upsloping", "Flat", "Downsloping"], help="Select the slope of the peak exercise ST segment.")

    with st.expander("ℹ️ Help"):
        st.write("ℹ️ **Age**: Enter the age of the patient in years.")
        st.write("ℹ️ **Sex**: Select the gender of the patient.")
        st.write("ℹ️ **Chest Pain Type**: Select the type of chest pain experienced by the patient.")
        st.write("ℹ️ **Resting Blood Pressure**: Enter the resting blood pressure of the patient in mmHg.")
        st.write("ℹ️ **Cholesterol**: Enter the cholesterol level of the patient in mg/dL.")
        st.write("ℹ️ **Fasting Blood Sugar**: Select the fasting blood sugar level of the patient.")
        st.write("ℹ️ **Resting ECG**: Select the resting electrocardiographic results of the patient.")
        st.write("ℹ️ **Max Heart Rate**: Enter the maximum heart rate achieved by the patient.")
        st.write("ℹ️ **Exercise-Induced Angina**: Select whether exercise-induced angina is present for the patient.")
        st.write("ℹ️ **Oldpeak**: Enter the ST depression induced by exercise relative to rest.")
        st.write("ℹ️ **ST Slope**: Select the slope of the peak exercise ST segment.")


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
