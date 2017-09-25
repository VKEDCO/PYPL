#!/usr/bin/python

################################
# module: TrajectoryUtils.py
# author: vladimir kulyukin
################################

import numpy as np
import cv2
import Utils
from EncircledContour import *
from Trajectory import *
from TrajectoryModel import TrajectoryModel as tm
from Background import subtractBackground

TRAJECTS = []

def findTrajectoryFor(xy, r, trajects, tick, tick_gap=1, delta=30):
    print 'Looking for traj for ec(c=', xy, ', r=', r, 't=', tick, ')'
    if len(trajects) == 0:
       print 'List of trajs is empty ...'
       return None
    else:
       for traj in trajects:
           if tm.isFeasibleFor(traj, xy, r, tick,
                               tick_gap=tick_gap, delta=delta):
              ecnt = traj.getEndContour()
              et = ecnt.getTick()
              return traj
       print 'No feasible trajs found ...'
       return None

## lower_r_bound and upper_r_bound control the size of the circle of
## the contour.
def processTrajects(frame, trajects, orig_frame, tick, direct, draw_flag,
                    lower_cnt_radius=3, upper_cnt_radius=15):
    cnts = cv2.findContours(frame.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)[-2]
    for cnt in cnts:
        xy, r = cv2.minEnclosingCircle(cnt)
        if lower_cnt_radius <= r <= upper_cnt_radius:
            t = findTrajectoryFor(xy, r, trajects, tick)
            k = EncircledContour(cnt, xy, r, tick=tick)
            if t is None:
               newt = Trajectory()
               newt.add(k)
               trajects.append(newt)
               if draw_flag is True:
                  ofc = orig_frame.copy()
                  utils.drawTrajectOnFrame(newt, ofc, tick, direct, imwrite_flag=True)
                  ofc2 = orig_frame.copy()
                  utils.drawTrajectsOnFrame(trajects, ofc2, tick, direct)
                  del ofc
                  del ofc2
            else:
               t.add(k)
               if draw_flag is True:
                  ofc = orig_frame.copy()
                  drawTrajectOnFrame(t, ofc, tick, direct, imwrite_flag=True)
                  ofc2 = orig_frame.copy()
                  drawTrajectsOnFrame(trajects, ofc2, tick, direct)
                  del ofc
                  del ofc2

def processFrame(frame, orig_frame, tick, direct, bckgrnd='MOG',
                 lower_cnt_radius=3, upper_cnt_radius=15,
                 draw_flag=True):
    sb = subtractBackground(frame, bckgrnd=bckgrnd)   
    processTrajects(sb, TRAJECTS, orig_frame, tick, direct, draw_flag)
    return Utils.findAndDrawContours(sb, orig_frame,
                                     lower_cnt_radius=lower_cnt_radius,
                                     upper_cnt_radius=upper_cnt_radius)

def processFrame2(frame, orig_frame, tick, direct, bckgrnd='MOG',
                  lower_cnt_radius=3, upper_cnt_radius=15, draw_flag=True):
    sb = subtractBackground(frame, bckgrnd=bckgrnd)
    processTrajects(sb, TRAJECTS, orig_frame, tick, direct, draw_flag)
    return Utils.findAndDrawContours2(sb, orig_frame,
                                      lower_cnt_radius=lower_cnt_radius,
                                      upper_cnt_radius=upper_cnt_radius)

def processContoursInFrame(frame, orig_frame, tick, direct,
                  lower_cnt_radius=1, upper_cnt_radius=3, draw_flag=True):
    sb = subtractBackgroundMOG(frame)
    return Utils.findAndDrawContours3(sb, orig_frame, lower_cnt_radius, upper_cnt_radius)
