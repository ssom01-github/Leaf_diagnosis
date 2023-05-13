import streamlit as st
import tensorflow as tf
from io import BytesIO
from PIL import Image
import numpy as np
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title='Leaf Disease Detection', page_icon=':leaves:')

# Load the pre-trained model
model=tf.keras.models.load_model('C:\\Users\\digital\\Desktop\\training1\\app_model (1).h5')

CLASS_NAMES = [
 'Potato_Early_blight',
 'Potato_late_blight',
 'Potato_healthy'
 ]

# Dictionary of diseases and their remedies
remedies = {
    "Potato_Early_blight":  "Remove infected leaves and use copper fungicides. Apply mulch to keep the soil moisture consistent.",
    "Potato_late_blight": "Copper-based fungicides along with organic remedies like neem oil and garlic extracts can also be used to control the spread of late blight in potato plants",
    "Potato_healthy": "Your leaf looks healthy! Keep up the good work!"
   
}


# Define the Streamlit app
st.title("Protect your plants, the smart way!! ")
# Upload the image
upload_file = st.file_uploader('Upload a image', type= ["png", "jpg","jpeg"])





if upload_file is not None:
    
    image = Image.open(upload_file)
    #image =image.resize((180, 180), resample=Image.BILINEAR)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
   
    #preprocess the image
    img = np.array(image.resize((256, 256)))
    img = np.expand_dims(img, axis=0)
    
    

    #make preduction using the model
    predictions = model.predict(img)[0]
    predicted_class = np.argmax(predictions)


    #get the predicted disease and its corresponding remedies
    predicted_disease = list(remedies.keys())[predicted_class]
    prediction_confidence = np.max(predictions)
    predicted_remedy = remedies[predicted_disease]



    #show the predicted disease and remedies
    st.write("The predicted disease is: " + predicted_disease)
    st.write("Confidence:", prediction_confidence)
    st.write("The remedy for this disease is: " + predicted_remedy)


    
    

    


    
    



    


    
    