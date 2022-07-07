import streamlit as st
import joblib
import requests
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from streamlit_player import st_player
import streamlit.components.v1 as components
from pipeline import Pipeline
model = joblib.load('model.sav')
transformer = joblib.load('transformer.sav')
pipe = Pipeline()
st.set_page_config(layout="wide")
with st.sidebar:
    
    choose = option_menu("Welcome", ["Home", "Tech Stack","Predictor","ML Code", "Contributors"],
                         icons=['house', 'calculator', 'exclamation-triangle','geo-alt', 'person lines fill'],
                         menu_icon='building', default_index=0, 
                         styles={
                            "container": {"padding": "5!important", "background-color": "#1a1a1a"},
                            "icon": {"color": "White", "font-size": "25px"}, 
                            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#4d4d4d"},
                            "nav-link-selected": {"background-color": "#4d4d4d"},
                        }
    ) 


with open("contributors.html",'r') as f:
   contributors=f.read();
def html():
    components.html(
      contributors
     ,
    height=1400,
    
    scrolling=True,
)
def pred():
    st.title("concrete-compressive-strength-estimator")
    
    
    cement = st.number_input("",max_value=1000000.0)
    st.write("Cement (number)")
    
    slag =st.number_input("",max_value=5000000.0)
    st.write("Slag")
    
    water=st.number_input("",max_value=7000000.0)
    st.write("Water")
    
    superplasticizer=st.number_input("",max_value=8000000.0)
    st.write("superplasticizer")
    
    age =st.number_input("",max_value=100000000.0)
    st.write("Age")
    
    
    st.write("")
    df = pipe.transform(cement, slag, water, superplasticizer, age)
    df = transformer.transform(df)

    
    if(st.button("Submit")):
        st.write((int(model.predict(df)[0])))
        

with open('techstack.html','r') as f:
  techstack=f.read();
def tech():
    components.html(
    techstack
    ,
    height=1000,
    
    scrolling=True,
    )
def ml():
  st.write("To view the complete code for the end-to-end project, visit our [GitHub](https://github.com/snshahgit/concrete-compressive-strength-estimator)")
  components.iframe("https://www.kaggle.com/embed/sns5154/ccse-validation-97-test-93?kernelSessionId=99431328",height=1000,)





if choose=="Predictor":

    pred()
elif choose=="Home":
    st.title('AI for Healthcare')
    st.markdown("<p style='text-align: justify;'>The objective of the project is to diagnostically predict whether or not a patient has Type 2 diabetes. \nThis predictor is built for Women above 21 years of age. The dataset, originally from the National Institute of Diabetes and Digestive and Kidney Diseases, used for this project consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.</p>", unsafe_allow_html=True)

    # st.markdown("<h1 style='text-align: center;'>Healthcare AI</h1>", unsafe_allow_html=True)

    with open("pic.html",'r') as f:
        pic=f.read();
    components.html(pic, height=400)

    # def load_lottieurl(url: str):
    #     r = requests.get(url)
    #     if r.status_code != 200:
    #         return None
    #     return r.json()
 
    # lt_url_hello = "https://assets6.lottiefiles.com/packages/lf20_1yy002na.json"
    # lottie_hello = load_lottieurl(lt_url_hello)
 
    # st_lottie(
    #         lottie_hello,  
    #         key="hello",
    #         speed=1,
    #         reverse=False,
    #         loop=True,
    #         quality="low",
    #         height=400,
    #         width=400            
    # )

    
elif choose=="Tech Stack":
    tech()
elif choose=="Contributors":
    html()
elif choose=="ML Code":
    ml()
