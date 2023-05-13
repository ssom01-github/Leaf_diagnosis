import PIL
import streamlit as st 
from PIL import Image
from streamlit_lottie import st_lottie
import requests


st.header("About Us ")
st.write("To detect the disease,read the image of the palnt. Identifies the disease of the leaves by extracting the region of interest of the image using dataset. Apply the Convolutional Neural Network Algorithm to classify on the basis of healthy and unhealthy leaves. We attained an accuracy of up to 98.02 percent, which is adequate for detecting illness in diverse leaves.")

st.info("This project is made by us....")

def load_lottieurl(url: str):
      r=requests.get(url)
      if r.status_code != 200:
        return None
      return r.json()
lottie_animation_2= "https://assets3.lottiefiles.com/private_files/lf30_8exlgvzr.json"
lottie_anim_json= load_lottieurl(lottie_animation_2)
st_lottie(lottie_anim_json, key="leaf",
            reverse=True,
          height=400,
          speed=1,
          loop=True,




)






