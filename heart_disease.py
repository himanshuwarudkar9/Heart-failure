import streamlit as st
import pickle

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

# Create a function to predict heart disease
def predict_heart_disease(attributes):
    # Preprocess the input attributes (if required)
    # ...

    # Make predictions using the loaded model
    prediction = model.predict(attributes)

    # Return the prediction
    return prediction

# Create the Streamlit app
def main():
    # Set the app title and description
    st.title("Heart Disease Prediction")
    st.write("Enter the patient's attributes to predict heart disease.")

    # Create input fields for the patient's attributes
    age = st.number_input("Age", min_value=1, max_value=100, value=30)
    sex = st.selectbox("Sex", ["Male", "Female"])
    chest_pain_type = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
    resting_bp = st.number_input("Resting Blood Pressure", min_value=80, max_value=200, value=120)
    cholesterol = st.number_input("Cholesterol", min_value=50, max_value=600, value=200)
    fasting_bs = st.selectbox("Fasting Blood Sugar", ["Lower than 120mg/dl", "Greater than 120mg/dl"])
    resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
    max_hr = st.number_input("Maximum Heart Rate", min_value=50, max_value=250, value=150)
    exercise_angina = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
    oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", value=0.0)
    st_slope = st.selectbox("ST Slope", ["Upsloping", "Flat", "Downsloping"])

    # Convert selected attributes to the format expected by the model
    # ...

    # Create a button to make predictions
    if st.button("Predict"):
        # Create a dictionary with the input attributes
        input_data = {
            'Age': age,
            'Sex': sex,
            'ChestPainType': chest_pain_type,
            'RestingBP': resting_bp,
            'Cholesterol': cholesterol,
            'FastingBS': fasting_bs,
            'RestingECG': resting_ecg,
            'MaxHR': max_hr,
            'ExerciseAngina': exercise_angina,
            'Oldpeak': oldpeak,
            'ST_Slope': st_slope
        }

        # Convert the dictionary to a DataFrame
        input_df = pd.DataFrame([input_data])

        # Make predictions
        prediction = predict_heart_disease(input_df)

        # Display the prediction
        if prediction[0] == 1:
            st.write("The patient is likely to have heart disease.")
        else:
            st.write("The patient is unlikely to have heart disease.")

# Run the app
if __name__ == '__main__':
    main()
