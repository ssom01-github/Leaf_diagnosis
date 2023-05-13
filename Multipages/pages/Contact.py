import streamlit as st
import requests
from streamlit_lottie import st_lottie

def contact():
    st.header("Contact Us")
    st.write("Please use the contact details below if you have any questions or concerns about our app.")
    st.write("Email: somrupas018@gmail.com")
   # st.write("Phone: +919358733048")
    
    st.write("You can also contact us on:")

    
    st.write("[LinkedIn](https://www.linkedin.com/in/somrupa-sarkar/)", )
    st.write("[Github](https://github.com/ssom01-github)")
    
    
    

if __name__ == '__main__':
    contact()



    def load_lottieurl(url: str):
       r=requests.get(url)
       if r.status_code != 200:
        return None
       return r.json()


lottie_animation_3= "https://assets7.lottiefiles.com/packages/lf20_pv4bovkh.json"
lottie_anim_json= load_lottieurl(lottie_animation_3)


st_lottie(lottie_anim_json, key="hello",
          reverse=True,
          height=200,
          width = 700,
          speed=1,
          loop=True,
          )