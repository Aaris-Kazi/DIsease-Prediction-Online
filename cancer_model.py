from joblib import load
from keras.preprocessing import image
from numpy import array

def can(img):
    rfc = load('models/multispec_rfc15.pkl')
    # img = imread(img)
    img = image.load_img(img)
    pimg = array(img).flatten()
    p = rfc.predict([pimg])
    if p[0] == '1':
        x = 'Positive'
    else:
        x = 'Negative'
    return x