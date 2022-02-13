import numpy as np
from keras.applications.mobilenet import preprocess_input
# import matplotlib.pyplot as plt
from keras.preprocessing import image
from keras.models import load_model

model = load_model("models/xray_model_final.h5")

def pretrained_path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # plt.imshow(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    x = np.expand_dims(x, axis=0)
    # convert RGB -> BGR, subtract mean ImageNet pixel, and return 4D tensor
    return preprocess_input(x)

def pneu(img):
    output = pretrained_path_to_tensor('upload/IM-0001-0001.jpeg')
    output = model(output)
    output = np.array(output)
    if np.argmax(output) == 1:
        print('The sample is positive')
    else:
        print('The sample is negative')