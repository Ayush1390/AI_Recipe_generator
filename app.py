from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient
import streamlit as st
import time

load_dotenv()
api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')

st.set_page_config(page_title="Recipe Recommender", layout="wide")

st.markdown("""
    <style>
        .stApp {
            background-image: url('https://png.pngtree.com/thumb_back/fh260/background/20200714/pngtree-modern-double-color-futuristic-neon-background-image_351866.jpg');
            background-size: cover;
            background-position: center;
        }

        .title {
            font-size: 60px;
            font-weight: bold;
            text-align: center;
            color:rgb(191, 181, 208);
            padding: 20px;
            text-shadow: 3px 3px 8px rgba(0, 0, 0, 0.5);
        }

        .header {
            font-size: 28px;
            font-weight: bold;
            color: #FFFFFF;
            margin-bottom: 20px;
        }

        .stTextInput>div>div>input {
            font-size: 18px;
            padding: 15px;
            border-radius: 10px;
            border: 2px solid #4CAF50; 
            background-color: rgb(23, 18, 87);
            color: #FFFFFF;
        }

        .stTextArea>div>div>textarea {
            font-size: 16px;
            padding: 10px;
            border-radius: 10px;
            border: 2px solid #4CAF50; 
            background-color: #1A1A1A; 
            color: #FFFFFF; 
        }

        .stButton>button {
            font-size: 20px;
            background-color: rgb(14, 86, 159); 
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .stButton>button:hover {
            background-color: rgb(88, 26, 233);
        }

        .stColumn {
            padding: 20px;
            background-color: rgba(26, 26, 26, 0.9); 
            border-radius: 10px;
            margin: 10px;
        }

        .stTextArea>div>div>textarea[disabled] {
            background-color: #1A1A1A;
            color: #FFFFFF !important;
            font-size: 16px;
            padding: 10px;
            border-radius: 10px;
            border: 2px solid #4CAF50;
            opacity: 1 !important;
        }

        .stTextArea>div>div>textarea[disabled]:hover {
            cursor: default;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Recipe Recommender</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<div class="header">Enter Ingredients</div>', unsafe_allow_html=True)
    elements = st.text_area(
        label="",
        placeholder="e.g., eggs, flour, sugar, milk, butter",
        height=200
    )
    button = st.button(label='Recommend')

if button:
    with col2:
        st.markdown('<div class="header">Recipe Steps</div>', unsafe_allow_html=True)
        with st.spinner('Generating recipe...'):
            time.sleep(2)

            client = InferenceClient(token=api_token)
            model_id = "mistralai/Mistral-7B-Instruct-v0.2"

            prompt = f"Generate a recipe from the following ingredients: {elements}. Also provide steps on how to make it."

            res = client.text_generation(prompt=prompt, model=model_id)

            recipe_output = res
            st.text_area(
                label="",
                value=recipe_output,
                height=400,
                disabled=True
            )