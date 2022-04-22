from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np 
from keras import backend as K
import streamlit as st


@st.cache(allow_output_mutation=True)
def load_trained_model():
    model = load_model('trained_models/resnext_50_transfer_learning.h5')
    # model._make_predict_function()
    session = K.get_session()
    return model, session

def predict(image1): 

    model, session = load_trained_model()

    K.set_session(session)
    
    img = Image.open(image1).resize((256,256))

    # convert the image pixels to a numpy array
    image = img_to_array(img)

    # Scale [0,1]
    scaled_image = (image - np.amin(image)) / (np.amax(image) - np.amin(image))

    # Init means and stds required by ResNeXt model
    means = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]

    # normalize image as per the means and stds above
    norm_image = (scaled_image - means)/std

    yhat = model.predict(np.expand_dims(norm_image, 0))

    if yhat[0][0] > yhat[0][1]:
        # Damage
        return ["Damage", yhat[0][0]] # [Label, Percentage]

    else:
        # Non-damage
        return ["Non-Damage", yhat[0][1]] # [Label, Percentage]
