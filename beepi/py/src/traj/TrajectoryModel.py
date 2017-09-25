#!/usr/bin/python

from scipy.spatial.distance import euclidean
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

class TrajectoryModel:

      @staticmethod
      def degAngleBetweenPoints(x1y1, x2y2):
          x1, y1 = x1y1
          x2, y2 = x2y2
          dx = x2 - x1
          dy = y2 - y1
          return math.atan2(dy, dx)*180/math.pi

      @staticmethod
      def degAngleBetweenStartAndEndContourCenters(traj):
          xsys = traj.getStartContour().getCenter()
          xeye = traj.getEndContour().getCenter()
          return TrajectoryModel.degAngleBetweenPoints(xsys, xeye)

      @staticmethod
      def isFeasibleFor(traj, xy, r, tick, tick_gap=1, delta=20.0):
          print 'Checking if', str(traj)
          print 'is feasible for ec(c=', xy, ', r=', r, 't=', tick, ')'
          print 'tick gap =', abs(tick - traj.getEndTick())
          if abs(tick - traj.getEndTick()) > tick_gap:
             print 'Tick gap is too wide'
             return False
          xeye = traj.getEndContour().getCenter()
          d = euclidean(xeye, xy)
          print 'distance=', d
          print 'd > delta?'
          print d > delta
          if d > delta:
             print 'Traj not feasible!'
             return False
          if traj.getNumContours() == 1:
             print 'Traj is feasible, because'
             print 'num contours in traject = 1'
             print 'Traj will be extended with ec(c=', xy, ', r=', r, 't=', tick, ')'
             #traj.setAngleSum(TrajectoryModel.degAngleBetweenPoints(xtyt, xy))
             return True
          else:
             a = TrajectoryModel.degAngleBetweenPoints(xeye, xy)
             print 'Traj possibly feasible'
             print 'Traj\'s angle=', a
             print 'Traj\'s angleSum=', traj.getAngleSum()
             # if the angle b/w the tail and xy is non-negative, i.e.,
             # the blob is detected south of the tail,
             # and the running sum of the traject is non-negative, i.e.,
             # south or flat.
             if 0<= a <= 180 and traj.getAngleSum() >=0:
                print '0<= a <= 180 and angleSum>=0'
                print 'Traj feasible!'
                return True
             # trajectory is going north and blob is
             # detected north of the tail.
             elif -179.9 <= a < 0 and traj.getAngleSum() < 0:
                print '-179.9 <= a < 0 and angleSum < 0'
                print 'Traj feasible!'
                return True
             else:
                print 'Traj not feasible, because both angleSum tests false'
                return False
            
      @staticmethod 
      def distanceOf(traj):
          xhyh = traj.getStartContour().getCenter()
          xtyt = self.geEndContour().getCenter()
          return euclidean(xhyh, xtyt)

      @staticmethod
      def isOutBound(traj, lowerTheta=-178.0, upperTheta=-2.0):
          ang = traj.getAngleSum()
          print ang, 'isOutBound?'
          if lowerTheta <= ang <= upperTheta:
             print 'isOutBound? Yes'
             return True
          else:
             print 'isOutBound? No'
             return False

      @staticmethod
      def isInBound(traj, lowerTheta=2.0, upperTheta=178.0):
          ang = traj.getAngleSum()
          print ang, 'isInBound?'
          if lowerTheta <= ang <= upperTheta:
             print 'isInBound? Yes'
             return True
          else:
             print 'isInBound? No'
             return False

      @staticmethod
      def isFlat(traj):
          ang = traj.getAngleSum()
          print ang, 'isFlat?'
          if not TrajectoryModel.isOutBound(traj) and \
             not TrajectoryModel.isInBound(traj):
             print 'isFlat? Yes'
             return True
          else:
             print 'isFlat? No'
             return False

      @staticmethod
      def isOutBound2(traj, lowerTheta=-178.0, upperTheta=-2.0):
          ang = traj.getAvrgAngle()
          print ang, 'isOutBound2?'
          if lowerTheta <= ang <= upperTheta:
             print 'isOutBound2? Yes'
             return True
          else:
             print 'isOutBound2? No'
             return False

      @staticmethod
      def isInBound2(traj, lowerTheta=2.0, upperTheta=178.0):
          ang = traj.getAvrgAngle()
          print ang, 'isInBound2?'
          if lowerTheta <= ang <= upperTheta:
             print 'isInBound2? Yes'
             return True
          else:
             print 'isInBound2? No'
             return False

      @staticmethod
      def isFlat2(traj):
          ang = traj.getAvrgAngle()
          print ang, 'isFlat2?'
          if not TrajectoryModel.isOutBound2(traj) and \
             not TrajectoryModel.isInBound2(traj):
             print 'isFlat2? Yes'
             return True
          else:
             print 'isFlat2? No'
             return False

      @staticmethod
      def isOutBound3(traj, lowerTheta=-178.0, upperTheta=-2.0):
          ang = traj.getAngleBetweenStartAndEnd()
          print ang, 'isOutBound3?'
          if lowerTheta <= ang <= upperTheta:
             print 'isOutBound3? Yes'
             return True
          else:
             print 'isOutBound3? No'
             return False

      @staticmethod
      def isInBound3(traj, lowerTheta=2.0, upperTheta=178.0):
          ang = traj.getAngleBetweenStartAndEnd()
          print ang, 'isInBound3?'
          if lowerTheta <= ang <= upperTheta:
             print 'isInBound3? Yes'
             return True
          else:
             print 'isInBound3? No'
             return False

      @staticmethod
      def isFlat3(traj):
          print ang, 'isFlat3?'
          if not TrajectoryModel.isOutBound3(traj) and \
             not TrajectoryModel.isInBound3(traj):
             print 'isFlat3? Yes'
             return True
          else:
             print 'isFlat3? No'
             return False

      @staticmethod
      def distanceOf(traj):
          xsys = traj.getStartContour().getCenter()
          xeye = traj.getEndContour().getCenter()
          return euclidean(xsys, xeye)

      @staticmethod
      def angleOf(traj):
          xsys = traj.getStartContour().getCenter()
          xeye = traj.getEndContour().getCenter()
          return TrajectoryModel.degAngleBetweenPoints(xsys, xeye)
