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
def predict_heart_disease(Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope):
    # Prepare the input data for prediction
    input_data = np.array([Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope]).reshape(1, -1)

    # Make prediction using the trained model
    prediction = model.predict(input_data)

    return prediction[0]

def main():
    st.markdown("<h1>Heart Disease Predictor</h1>", unsafe_allow_html=True)
    st.markdown("<p>Enter the values for various attributes to predict the presence of heart disease.</p>", unsafe_allow_html=True)

    # Create input fields for the heart disease attributes
    Age = st.number_input("Age", min_value=0, max_value=120, step=1)
    Sex = st.selectbox("Sex", ["Male", "Female"])
    ChestPainType = st.selectbox("Chest Pain Type", ["ASY", "NAP", "ATA", "TA"])
    RestingBP = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, step=1)
    Cholesterol = st.number_input("Serum Cholesterol (mg/dL)", min_value=0, step=1)
    FastingBS = st.selectbox("Fasting Blood Sugar > 120 mg/dL", ["False", "True"])
    RestingECG = st.selectbox("Resting Electrocardiographic Results", ["Normal", "LVH", "ST"])
    MaxHR = st.number_input("Maximum Heart Rate Achieved", min_value=0, step=1)
    ExerciseAngina = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
    Oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, step=0.1)
    ST_Slope = st.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
   

    # Convert categorical inputs to numerical values
    Sex = 1 if Sex == "Male" else 0
    ChestPainType = {"ASY": 0, "NAP": 1, "ATA": 2, "TA": 3}
    ChestPainType = ChestPainType[ChestPainType]
    FastingBS = 1 if fbs == "True" else 0
    RestingECG_mapping = {"Normal": 0, "LVH": 1, "ST": 2}
    RestingECG = RestingECG_mapping[RestingECG]
    exang = 1 if exang == "Yes" else 0
    ST_Slope_mapping = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
    ST_Slope = ST_Slope_mapping[ST_Slope]
   

    # Perform heart disease prediction when the user clicks the "Predict" button
    if st.button("Predict"):
        prediction = predict_heart_disease(Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope)
        if prediction == 1:
            st.markdown("<p>The model predicts that the person has <strong>heart disease</strong>.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p>The model predicts that the person does <strong>not have heart disease</strong>.</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
