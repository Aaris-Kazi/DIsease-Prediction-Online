from joblib import load
from cv2 import imread
# import numpy as np
from numpy import array

def can(img):
    rfc = load('models/multispec_rfc15.pickle')
    img = imread('upload/'+img)
    pimg = array(img).flatten()
    p = rfc.predict([pimg])
    if p[0] == '1':
        x = 'Positive'
    else:
        x = 'Negative'
    # plt.imshow(img)
    # v = plt.show()
    return x
# plt.title(x)