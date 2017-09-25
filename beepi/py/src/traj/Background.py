#!/usr/bin/python

import numpy as np
import cv2
import Utils

MOG_HISTORY = 200
MOG_NMIXTURES = 5
MOG_BCKGRND_RATIO = 0.7
MOG_NOISE_SIGMA = 0

MOG = cv2.bgsegm.createBackgroundSubtractorMOG(history=MOG_HISTORY,
                                               nmixtures=MOG_NMIXTURES,
                                               backgroundRatio=MOG_BCKGRND_RATIO,
                                               noiseSigma=MOG_NOISE_SIGMA)

MOG2 = cv2.createBackgroundSubtractorMOG2()


KERNEL = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
KNN = cv2.createBackgroundSubtractorKNN()

def subtractBackgroundMOG(frame):
    global MOG
    foregroundMask = MOG.apply(frame)
    return foregroundMask

def subtractBackgroundMOG2(frame):
    global MOG2
    foregroundMask = MOG2.apply(frame)
    return foregroundMask

def subtractBackgroundKNN(frame):
    global KNN
    global KERNEL
    fgmask = KNN.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, KERNEL)
    return fgmask

def subtractBackground(frame, bckgrnd='MOG'):
    if bckgrnd == 'MOG':
        sb = subtractBackgroundMOG(frame)
    elif bckgrnd == 'MOG2':
        sb = subtractBackgroundMOG2(frame)
    else:
        sb = subtractBackgroundKNN(frame)
    return sb
