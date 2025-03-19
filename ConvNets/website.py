import streamlit as st
import numpy as np
import tensorflow as tf
import keras
from PIL import Image
from keras.src.utils.module_utils import tensorflow

model = tensorflow.keras.models.load_model('model2.h5')

st.title('CNN Gender Classifier')

image_file = st.file_uploader('Upload Image', type=['png', 'jpg', 'jpeg'])

if image_file is not None:
    image = Image.open(image_file)
    st.image(image_file, use_container_width=True)

    image = image.convert('RGB')
    image = image.resize((200, 200))
    image = np.array(image) / 255
    image = np.expand_dims(image, axis=0)

if st.button('Predict'):
    prediction = model.predict(image)
    # gender = 'Male' if prediction[0][0] >= 0.5 else 'Female' : use this when using model 1(made use of the sigmoid function)
    gender = 'Female' if np.argmax(prediction) == 0 else 'Male' #for model 2 which made use of the softmax function at the output layer
    st.write(f'Predicted Gender: {gender}')
    st.write(prediction)