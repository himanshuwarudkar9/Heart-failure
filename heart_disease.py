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

# Load trained model from pickle file
def load_model():
    with open('trained_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Main Streamlit app code
def main():
    # Set app title
    st.title("Heart Disease Classification")
    
    # Load the trained model
    model = load_model()

    # Add a sidebar
    st.sidebar.title("Attribute Ranges")
    
    # Display attribute ranges in the sidebar
    attribute_ranges = {
        'Age': '29-76',
        'Sex': 'Male (1), Female (0)',
        'ChestPainType': 'Typical angina, Atypical angina, Non-anginal pain, N/A',
        'RestingBP': '94-145 mmHg',
        'Cholesterol': '126-564 mg/dL',
        'FastingBS': 'True (1), False (0)',
        'RestingECG': 'N/A',
        'MaxHR': '71-202 bpm',
        'ExerciseAngina': 'No (0), Yes (1)',
        'Oldpeak': '0.0-3.5',
        'ST_Slope': 'N/A',
        'HeartDisease': 'No (0), Yes (1)'
    }
    
    for attribute, range_info in attribute_ranges.items():
        st.sidebar.text(f"{attribute} Range: {range_info}")
    
    # Display the trained model
    st.header("Heart_failure.pkl")
    st.write(model)
    
if __name__ == "__main__":
    main()
