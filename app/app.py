import streamlit as st 
from PIL import Image
from classify import predict


st.title("COMP6604 Project Demo")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.header("Results")
    with st.spinner('Classifying...'):
        label = predict(uploaded_file)
    
    st.write('%s (%.2f%%)' % (label[0], label[1]*100))