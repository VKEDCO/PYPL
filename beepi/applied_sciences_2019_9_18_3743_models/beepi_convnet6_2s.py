###################################################################
# module: beepi_convnet6_2s.py
#
# description: loading and running ConvNet6_2s model.
# See the article: V. Kulyukin, S. Mukherjee. "On Video Analysis of
# Omnidirectional Bee Traffic: Counting Bee Motions with Motion
# Detection and Image Classification." Applied Sciences, 2019, 9(18),
# 3743; https://doi.org/10.3390/app9183743.
#
# author: Vladimir Kulyukin
#
# to run:
# python beepi_convnet6_2s.py <path_to_png_image>
#
# example:
# python beepi_convnet6_2s.py yb.png
# loading ConvNet6_2s model...
# ... some tf output
# ConvNet6_2s loaded...
# bee_probability    = 0.9827054738998413
# no_bee_probability = 0.017294451594352722
###################################################################

import cv2
import sys
import tensorflow as tf
import numpy as np
from beepi_convnets import beepi_convnets

BEE    = 0
NO_BEE = 1

IMWIDTH   = 64
IMHEIGHT  = 64
IMCHANNEL = 3

# directory with persisted trained models
PERSISTED_DIR = '../models/'

tf.reset_default_graph()

model_name = 'ConvNet6_2s'
print('loading {} model...'.format(model_name))
dnn_model = beepi_convnets.ConvNet6(IMWIDTH, IMHEIGHT, IMCHANNEL)
dnn_model.load(PERSISTED_DIR + model_name + '.tfl')
print('{} loaded...'.format(model_name))

def preprocess_image(image, width, height):
    """
    Takes a OpenCV image, its width and height; resizes to the dimensions
    required by the classification model.
    """
    x = []
    if image.shape[0] > 0 and image.shape[1] > 0:
        image = cv2.resize(image, (width, height))
        x.append(image)
        x = np.array(x, dtype='float') / 255.0
        return x
    else:
        return None

def classify_image(dnn_model, img_path):
    """
    Reads in an OpenCV image saved in img_path, pre-processes it,
    and and predicts its label with dnn_model.
    """
    global IMWIDTH
    global IMHEIGHT
    img = cv2.imread(img_path)
    assert img is not None
    img = preprocess_image(img, IMWIDTH, IMHEIGHT)
    prediction = dnn_model.predict(img)
    return prediction

if __name__ == '__main__':
    prediction = classify_image(dnn_model, sys.argv[1])
    yes_bee, no_bee = prediction[0][BEE], prediction[0][NO_BEE]
    print('bee_probability    = {}'.format(yes_bee))
    print('no_bee_probability = {}'.format(no_bee))
    pass
