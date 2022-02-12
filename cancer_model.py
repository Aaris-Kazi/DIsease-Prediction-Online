from joblib import load
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def can(img):
    rfc = load('multispec_rfc15.pickle')
    img = cv.imread('upload/'+img)
    pimg = np.array(img).flatten()
    p = rfc.predict([pimg])
    if p[0] == '1':
        x = 'Positive'
    else:
        x = 'Negative'
    return x
# plt.title(x)
# plt.imshow(img)
# plt.show()