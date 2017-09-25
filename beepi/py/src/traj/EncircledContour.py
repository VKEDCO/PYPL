#!/usr/bin/python

#####################################
# module: EncircledContour.py
# author: vladimir kulyukin
#####################################

class EncircledContour:
      def __init__(self, points, xy, r, tick=0):
          self.points = points
          self.center = xy
          self.radius = r
          self.tick = tick

      def getPoints(self):
          return self.points

      def getCenter(self):
          return self.center

      def getRadius(self):
          return self.radius

      def getTick(self):
          return self.tick

      def __str__(self):
          return 'ec(c=' + str(self.center) + \
                 ', r=' + str(self.radius) + \
                 ', t=' + str(self.tick) +')'
