from joblib import load
import cv2 as cv
import numpy as np

def can(img):
    rfc = load('models/multispec_rfc15.pickle')
    img = cv.imread('upload/'+img)
    pimg = np.array(img).flatten()
    p = rfc.predict([pimg])
    if p[0] == '1':
        x = 'Positive'
    else:
        x = 'Negative'
    # plt.imshow(img)
    # v = plt.show()
    return x
# plt.title(x)