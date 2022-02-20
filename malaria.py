import numpy as np
from keras.applications.mobilenet import preprocess_input
# import matplotlib.pyplot as plt
from keras.preprocessing import image
from keras.models import load_model

model = load_model("models/malaria_cnn.h5")

def mala(img):
    img = image.load_img(img, target_size=(50, 50))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    output = preprocess_input(x)
    output = model(output)
    output = np.array(output)
    if np.argmax(output) == 0:
        v = 'The sample is positive'
    else:
        v = 'The sample is negative'
    return v