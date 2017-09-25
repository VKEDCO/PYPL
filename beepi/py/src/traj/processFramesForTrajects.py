#!/usr/bin/python

###############################################
# module: processFramesForTrajects.py
# author: vladimir kulyukin
# usage:
#
# the contour sizes are controlled in
# TrajectoryUtils.processTrajects(). The call
# chain is
# TrajectoryUtils.processTrajects() ->
# TrajectoryUtils.processFrame() ->
# TrajectoryUtils.processTrajects()
###############################################

import numpy as np
import argparse
import utils
import cv2
from EncircledContour import *
from Trajectory import *
from TrajectoryModel import TrajectoryModel as tm
import TrajectoryUtils as trajutils
from os import listdir
from os.path import isfile, join, splitext
import os

'''
python processFramesForTrajects.py
-id ir/HamorsPass/BACKUP/EBM/eval/REFRAMES_May_09/192_168_4_8-2017-05-09_15-00-28/
-od /media/vladimir/HamorsPass/BACKUP/EBM/eval/REFRAMES_May_09/192_168_4_8-2017-05-09_15-00-28_traj/
'''

'''
I need to do two things: 1) figure out how to control the radius of the contour and
how to count contours.
'''

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-id', '--input_dir',
                help='path to the dir where frames are saved',
                required=True)
ap.add_argument('-od', '--output_dir',
                help='path where the output images are saved',
                required=True)

args      = vars(ap.parse_args())
FRAME_DIR = args['input_dir']
DIRECT    = args['output_dir']

if not os.path.exists(DIRECT):
      os.makedirs(DIRECT)

ORIG_FRAME = None
TICK = 0
IMG_FILES = [f for f in listdir(FRAME_DIR)
             if isfile(join(FRAME_DIR, f))]
IMG_FILES.sort(key=lambda f: int(splitext(f)[0].split('_')[-1]))

SAVE_EACH_FRAME_FLAG  = False
LOWER_CNT_RADIUS = 3
UPPER_CNT_RADIUS = 15
BCKGRND = 'MOG' # other values are 'MOG2', 'KNN'.

# keep looping
for f in IMG_FILES:
      frame = cv2.imread(join(FRAME_DIR, f))
      print
      print '*****Processing frame', join(FRAME_DIR, f), TICK
      cv2.imshow('Current Frame', frame)
      if ORIG_FRAME is None:
         ORIG_FRAME = frame
      pf = trajutils.processFrame(frame, frame.copy(), TICK, DIRECT,
                                  bckgrnd=BCKGRND,
                                  lower_cnt_radius=LOWER_CNT_RADIUS,
                                  upper_cnt_radius=UPPER_CNT_RADIUS,
                                  draw_flag=False)
      if SAVE_EACH_FRAME_FLAG:
            cv2.imwrite(DIRECT + 'frame_' + str(TICK) + '.png', pf)
      cv2.imshow("Current Frame", pf)
      TICK += 1
      key = cv2.waitKey(1) & 0xFF
      # if the 'q' key is pressed, stop the loop
      if key == ord('q'):
         break

TRAJECTS = trajutils.TRAJECTS
TRAJECTS.sort(key=lambda t: t.getNumContours(), reverse=True)
print len(TRAJECTS)
for t in TRAJECTS[:20]:
    print len(t.contours), 'contours'
       
utils.drawAndSaveTrajectsInFiles(TRAJECTS, ORIG_FRAME, DIRECT)
