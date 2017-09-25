#!/usr/bin/python

##################################
# module: Utils.py
# author: vladimir kulyukin
##################################

import numpy as np
import cv2
from scipy.spatial.distance import euclidean
import math
from EncircledContour import *
from Trajectory import *

def findAndDrawContours(frame, orig_frame,
                        lower_cnt_radius=3, upper_cnt_radius=15):
    cnts = cv2.findContours(frame.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
       for c in cnts:
           # find the largest contour in the mask, then use
           # it to compute the minimum enclosing circle and
           # centroid
           # c = max(cnts, key=cv2.contourArea)
           ((x, y), radius) = cv2.minEnclosingCircle(c)
           #M = cv2.moments(c)
           #center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
           # only proceed if the radius meets a minimum size
           #print("radius = %s" % str(radius))
           if lower_cnt_radius <= radius <= upper_cnt_radius:
              # draw the circle and centroid on the frame,
              # then update the list of tracked points
              cv2.circle(orig_frame, (int(x), int(y)), int(radius),
                        (0, 255, 255), 2)
              #cv2.circle(frame, center, 5, (0, 0, 255), -1)
    return orig_frame

def findAndDrawContours2(frame, orig_frame, lower_cnt_radius, upper_cnt_radius):
    cnts = cv2.findContours(frame.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
       for c in cnts:
           # find the largest contour in the mask, then use
           # it to compute the minimum enclosing circle and
           # centroid
           # c = max(cnts, key=cv2.contourArea)
           ((x, y), radius) = cv2.minEnclosingCircle(c)
           #M = cv2.moments(c)
           #center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
           # only proceed if the radius meets a minimum size
           #print("radius = %s" % str(radius))
           if lower_cnt_radius <= radius <= upper_cnt_radius:
              # draw the circle and centroid on the frame,
              # then update the list of tracked points
              cv2.circle(orig_frame, (int(x), int(y)), int(radius),
                        (0, 255, 255), 2)
              #cv2.circle(frame, center, 5, (0, 0, 255), -1)
    return orig_frame

def findAndDrawContours3(frame, orig_frame, lower_cnt_radius, upper_cnt_radius):
    cnts = cv2.findContours(frame.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    cnt_count = 0
    # only proceed if at least one contour was found
    if len(cnts) > 0:
       for c in cnts:
           # find the largest contour in the mask, then use
           # it to compute the minimum enclosing circle and
           # centroid
           # c = max(cnts, key=cv2.contourArea)
           ((x, y), radius) = cv2.minEnclosingCircle(c)
           #M = cv2.moments(c)
           #center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
           # only proceed if the radius meets a minimum size
           #print("radius = %s" % str(radius))
           if lower_cnt_radius <= radius <= upper_cnt_radius:
              # draw the circle and centroid on the frame,
              # then update the list of tracked points
              cv2.circle(orig_frame, (int(x), int(y)), int(radius),
                        (0, 255, 255), 2)
              cnt_count += 1
              #cv2.circle(frame, center, 5, (0, 0, 255), -1)
    return cnt_count, orig_frame

def drawTrajectOnFrame(traj, frame, tick, direct, imwrite_flag=False):
    nc = traj.getNumContours()
    if nc == 0: return
    prevCnt = traj.contours[0]
    pr = prevCnt.getRadius()
    px, py = prevCnt.getCenter()
    cv2.circle(frame, (int(px), int(py)), int(pr),
                  (0, 255, 255), 2)

    if nc > 1: 
       for currCnt in traj.contours[1:]:
           cx, cy = currCnt.getCenter()
           cr = currCnt.getRadius()
           cv2.circle(frame, (int(cx), int(cy)), int(cr),
                      (0, 255, 255), 2)
           cv2.line(frame, (int(px), int(py)), (int(cx), int(cy)),
                    (0, 255, 255), 2)
           px = cx
           py = cy
           pr = cr

    if imwrite_flag is True:
       cv2.imwrite(direct + 'frame_traject_at_' + str(tick) + '.png', frame)

# draw trajectories
def drawTrajectsOnFrame(trajects, frame, tick, direct):
    for tn, t in enumerate(trajects):
        drawTrajectOnFrame(t, frame, tn, direct, imwrite_flag = False)
    cv2.imwrite(direct + 'frame_all_trajects_at_' + str(tick) + '.png',
                frame)

def drawAndSaveTrajectInFile(traj, frame, direct,
                             isInBound=tm.isInBound3,
                             isOutBound=tm.isOutBound3):
    nc = traj.getNumContours()
    print 'Drawing traj with', str(nc), 'contours'
    d = int(math.ceil(tm.distanceOf(traj)))
    if nc == 0: return
    prevCnt = traj.getIthContour(0)
    pr = prevCnt.getRadius()
    px, py = prevCnt.getCenter()
    cv2.circle(frame, (int(px), int(py)), int(pr),
                  (0, 255, 255), 2)

    if nc > 1: 
       for currCnt in traj.getContours()[1:]:
           cx, cy = currCnt.getCenter()
           cr = currCnt.getRadius()
           cv2.circle(frame, (int(cx), int(cy)), int(cr),
                      (0, 255, 255), 2)
           cv2.line(frame, (int(px), int(py)), (int(cx), int(cy)),
                    (0, 255, 255), 2)
           px = cx
           py = cy
           pr = cr

    trajDirection = '_unk'
    if isInBound(traj):
       trajDirection = '_in'
    elif isOutBound(traj):
       trajDirection = '_out'
    else:
       trajDirection = '_flat'

    cv2.imwrite(direct + 'tj_nc_' + str(nc) \
                + trajDirection \
                + '_d_' + str(d) \
                + '_aa_' + str(int(traj.getAvrgAngle())) \
                + '_ase_' + str(int(traj.getAngleBetweenStartAndEnd())) \
                + '_ar_' + str(int(traj.getAvrgCntRadius())) \
                + '_st_' + str(traj.getStartTick()) \
                + '_et_' + str(traj.getEndTick()) + '.png', frame)

def drawAndSaveTrajectsInFiles(trajects, frame, direct):
    for tj in trajects:
        fc = frame.copy()
        drawAndSaveTrajectInFile(tj, fc, direct)
