import streamlit as st
import numpy as np
import pickle

# Load a pre-trained model (replace 'model.pkl' with the actual file if you have it)
# For demonstration, we assume the model is a simple linear regression model.
# def load_model():
#     # Replace this with the actual model loading code
#     with open('model.pkl', 'rb') as file:
#         model = pickle.load(file)
#     return model

# model = load_model()

def predict_premium(age, sex, bmi, children, smoker, region):
    """
    Predict the insurance premium using the pre-trained model.

    Parameters:
        age (int): Age of the individual
        sex (str): Male or Female
        bmi (float): Body Mass Index
        children (int): Number of children
        smoker (str): Yes or No
        region (str): One of the predefined regions

    Returns:
        float: Predicted insurance premium
    """
    # Convert categorical inputs into numeric values
    sex_num = 1 if sex == 'Male' else 0
    smoker_num = 1 if smoker == 'Yes' else 0
    region_map = {'Northeast': 0, 'Northwest': 1, 'Southeast': 2, 'Southwest': 3}
    region_num = region_map[region]

    # Prepare the input features as a numpy array
    features = np.array([[age, sex_num, bmi, children, smoker_num, region_num]])

    # Predict using the loaded model
    premium = model.predict(features)[0]
    return premium

# Streamlit frontend
st.title("AI-Driven Medical Insurance Premium Predictor")
st.sidebar.header("Input Parameters")

# Sidebar inputs
age = st.sidebar.slider("Age", min_value=18, max_value=100, value=30, step=1)
sex = st.sidebar.selectbox("Sex", options=["Male", "Female"])
bmi = st.sidebar.slider("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
children = st.sidebar.slider("Number of Children", min_value=0, max_value=5, value=0, step=1)
smoker = st.sidebar.selectbox("Smoker", options=["Yes", "No"])
region = st.sidebar.selectbox(
    "Region",
    options=["Northeast", "Northwest", "Southeast", "Southwest"]
)
st.subheader("Selected Input Values")
st.write(f"**Age:** {age}")
st.write(f"**Sex:** {sex}")
st.write(f"**BMI:** {bmi}")
st.write(f"**Number of Children:** {children}")
st.write(f"**Smoker:** {smoker}")
st.write(f"**Region:** {region}")
# Button to trigger prediction
if st.sidebar.button("Predict Premium"):
    premium = predict_premium(age, sex, bmi, children, smoker, region)
    st.success(f"The predicted insurance premium is: ${premium:.2f}")

# Additional information section
st.info(
    "This app predicts medical insurance premiums using a pre-trained machine learning model. "
    "Adjust the input parameters on the sidebar to see the prediction."
)
