#!/usr/bin/python

from scipy.spatial.distance import euclidean
from TrajectoryModel import TrajectoryModel as tm
import math

##############################
#
#
#            -90
#             |
#             |
#             |
#             |
# +180 <-----------------> 0
#             |
#             |
#             |
#             V
#            +90
#
#
# author: vladimir kulyukin
###############################

import time

class Trajectory:
      def __init__(self):
          self.contours = []
          self.angleSum = 0.0
          self.time = int(time.time())
          print 'New Traj created at time', str(self.time)

      def getContours(self):
          return self.contours
      
      def getStartContour(self):
          return self.contours[0]

      def getEndContour(self):
          return self.contours[-1]

      def getNumContours(self):
          return len(self.contours)

      def getId(self):
          if len(self.contours) == 0:
             return (self.time, None, None)
          else:
             return (self.time, self.getStartContour(),
                     self.getEndContour())

      def getAvrgAngle(self):
          if len(self.contours) == 0 or len(self.contours) == 1:
             return 0
          else:
             return float(self.angleSum) / (len(self.contours)-1)

      def getAngleBetweenStartAndEnd(self):
          xsys = self.getStartContour().getCenter()
          xeye = self.getEndContour().getCenter()
          return tm.degAngleBetweenPoints(xsys, xeye) 

      def getEndTick(self):
          return self.getEndContour().getTick()

      def getStartTick(self):
          return self.getStartContour().getTick()

      def getAngleSum(self):
          return self.angleSum

      def setAngleSum(self, v):
          self.angleSum = v

      def incrementAngleSum(self, v):
          self.angleSum += v
       
      def add(self, ek):
          print 'Adding', str(ek), 'to', str(self)
          self.contours.append(ek)
          if self.getNumContours() > 1:
             print 'Since num contours in', str(self), '> 1,'
             print 'angleSum will be updated...'
             xsys = self.getStartContour().getCenter()
             xeye = ek.getCenter()
             a = tm.degAngleBetweenPoints(xsys, xeye)
             print 'a =', a
             self.incrementAngleSum(a)
             print 'self.angleSum =', self.getAngleSum()

      def getIthContour(self, i):
          return self.contours[i]

      def getAvrgCntRadius(self):
          if self.getNumContours() == 0:
             return 0
          radSum = 0
          for ecnt in self.contours:
              radSum += ecnt.getRadius()
          return radSum / self.getNumContours()

      def __str__(self):
          t, scnt, ecnt = self.getId()
          if scnt is None and ecnt is None:
             return 'Traj(' + str(t) + '0' + '0)'
          else:
             return 'Traj(' + str(t) + ', ' + str(scnt) + ', ' + str(ecnt) + ')'
      

