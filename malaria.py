from numpy import array, expand_dims, argmax
from keras.applications.mobilenet import preprocess_input
from keras.preprocessing import image
from keras.models import load_model

def malar(img):
    model = load_model("models/malaria_cnn.h5")
    img = image.load_img(img, target_size=(50, 50))
    x = image.img_to_array(img)
    x = expand_dims(x, axis=0)
    output = preprocess_input(x)
    output = model(output)
    output = array(output)
    if argmax(output) == 0:
        v = 'The sample is positive'
    else:
        v = 'The sample is negative'
    return v