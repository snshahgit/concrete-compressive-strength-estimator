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
                         icons=['house', 'stack', 'cpu','terminal', 'people-fill'],
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
    st.title("CONCRETE COMPRESSIVE STRENGTH ESTIMATOR")
    
    
    cement = st.number_input("",min_value= 0.0, max_value=700.0)
    st.write("Quantity of Cement (kgs in a cubic meter mixture)")
    
    slag =st.number_input("",min_value= 0.0, max_value=450.0)
    st.write("Quantity of Slag (kgs in a cubic meter mixture)")
    
    water=st.number_input("",min_value= 0.0, max_value=350.0)
    st.write("Quantity of Water (kgs in a cubic meter mixture)")
    
    superplasticizer=st.number_input("",min_value= 0.0, max_value=70.0)
    st.write("Quantity of Superplasticizer (kgs in a cubic meter mixture)")
    
    age =st.slider("",0,364,step =7)
    st.write("Age of the mixture (in days)")
    
    
    st.write("")
    df = pipe.transform(cement, slag, water, superplasticizer, age)
    df = transformer.transform(df)

    
    if(st.button("Submit")):
        st.info(f'**The compressive strenth of the concrete mixture is {(int(model.predict(df)[0]))} MPa**')
        

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
    st.title('AI for InfraTech')
    st.write('')

    st.subheader("Public Good")
    st.markdown("<p style='text-align: justify;'>Concrete takes lot of time to set and harden. Often due to strict timelines, supervisors force the workers to start working even when the concrete hasn't hardened. This leads to collapsing of pre-mature structures. Such scenario has a fatal potent which can cause harm to poor workers who don't even have a basic medical coverage.</p>", unsafe_allow_html=True)

    st.write('')
    st.write('')
    st.subheader("What's the solution ?")
    st.markdown("<p style='text-align: justify;'>This project aims to predict the compressive strength of concrete using parameters such as: quantity of cement, flyash, water, superplasticizer, coarse and fine aggregate, and the age of the mixture.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>The user can permute over different values of raw inputs and make an optimal concrete mixture that guarantees the required compressive strenth. User can also optimize the concrete mixture such that the cost is minimal.</p>", unsafe_allow_html=True)

    # st.markdown("<h1 style='text-align: center;'>Healthcare AI</h1>", unsafe_allow_html=True)

    # with open("pic.html",'r') as f:
    #     pic=f.read();
    # components.html(pic, height=400)

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
