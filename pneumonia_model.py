from numpy import array, expand_dims, argmax
from keras.applications.mobilenet import preprocess_input
from keras.preprocessing import image
from keras.models import load_model

def pneumo(img):
    model = load_model("models/xray_model_final.h5")
    img = image.load_img(img, target_size=(224, 224))
    x = image.img_to_array(img)
    x = expand_dims(x, axis=0)
    output = preprocess_input(x)
    output = model(output)
    output = array(output)
    if argmax(output) == 1:
        v = 'The sample is positive'
    else:
        v = 'The sample is negative'
    return v