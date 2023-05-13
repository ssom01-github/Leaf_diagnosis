import PIL
import streamlit as st 
from PIL import Image
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Plant detection & prediction")



def load_lottieurl(url: str):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_animation_1= "https://assets5.lottiefiles.com/packages/lf20_9evakyqx.json"
lottie_anim_json= load_lottieurl(lottie_animation_1)


st_lottie(lottie_anim_json, key="hello",
          reverse=True,
          height=300,
          speed=1,
          loop=True,
          )




st.header("Welcome to Leaf diagnosis App " )

st.write("upload the image to detect the disease")




rad= st.radio(
    "Services ",
    ("Leaf diagnosis", "Consultancy with Expert"),horizontal= True
    )

if rad == 'Leaf diagnosis':
    st.write("Kindly move to main app")
    
else:
    st.write("This part is coming soon.")

#Image= Image.open('C:\\Users\\digital\\Desktop\\training1\\Multipages\\agri.jpg')
#st.image(Image, caption='Saving the crops')









