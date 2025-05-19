import streamlit as st
import base64
from PIL import Image

# Function to load image and convert it to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load the logo and display
@st.cache_data
def load_image(image_path):
    return Image.open(image_path)

logo = load_image("./logo.png")
st.image(logo)

st.write("TCM-EnvNephroToxPred: A Computational Tool for Renal Toxicity Evaluation of Environmentally Relevant Traditional Chinese Medicine Compounds
Developed through interdisciplinary collaboration, this predictive model assesses nephrotoxic risks in herbal-derived environmental contaminants.")

st.write("Research Support: This work was enabled by computational infrastructure and expertise from Pro. Xiuqing Zhu, AI-Drug Lab, Brain Hospital Affiliated to Guangzhou Medical University, China.")

st.write("Contact: For scientific inquiries or collaborative opportunities, please contact: Pro. Xiuqing Zhu
Email: 2018760376@gzhmu.edu.cn")

st.title("Nephrotoxic Component Predictor")

# Load images for buttons and convert to base64
single_img_base64 = get_base64_image("./single_image.png")
batch_img_base64 = get_base64_image("./batch_image.png")

# Set up columns for layout
col1, col2 = st.columns(2)

# Add buttons with background images and hyperlinks
with col1:
    st.markdown(
        f"""
        <style>
        .single-button {{
            background-image: url("data:image/png;base64,{single_img_base64}");
            background-size: cover;
            height: 300px;
            width: 90%;
            border: yes;
            color: black;
            font-family: Arial, sans-serif;
            font-size: 20px;
            font-weight: bold;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }}
        </style>
        <div class="single-button">
            <a href="https://nephrotoxpredictor-single.streamlit.app/" target="_blank" style="color:black; text-decoration: none;">Click for Single Compound Prediction</a>
        </div>
        """, 
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <style>
        .batch-button {{
            background-image: url("data:image/png;base64,{batch_img_base64}");
            background-size: cover;
            height: 300px;
            width: 90%;
            border: yes;
            color: black;
            font-family: Arial, sans-serif;
            font-size: 20px;
            font-weight: bold;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }}
        </style>
        <div class="batch-button">
            <a href="https://nephrotoxpredictor-batch.streamlit.app/" target="_blank" style="color:black; text-decoration: none;">Click for Batch Compound Prediction</a>
        </div>
        """, 
        unsafe_allow_html=True
    )
