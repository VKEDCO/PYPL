import math
import random
import scipy as sp
import cv2

###############################################################################################
# Module: NumUtils.py
# Author: Vladimir Kulyukin, Vikas Reddy
# Added getImageRow, get_angle, get_distance, draw_spikes, draw_spikes, and draw_line
###############################################################################################

class NumUtils:

    @staticmethod
    def isPowOf2(n):
        if n < 1:
            return False
        else:
            pOf2 = (math.log(n) / math.log(2))
            return math.fabs(pOf2 - int(pOf2)) == 0

    @staticmethod
    def intLog2(n):
        return int(math.log(n) / math.log(2))

    @staticmethod
    def genListOfRandomInts(a, b, num_elems):
        return [random.randint(a, b) for i in xrange(num_elems)]

    @staticmethod
    def areEqualLists(lst1, lst2):
        if len(lst1) != len(lst2):
            return False
        for x, y in zip(lst1, lst2):
            if x - y != 0:
                return False
        return True

    @staticmethod
    def padWithZerosToPowOf2(signal):
        length = len(signal)
        if NumUtils.isPowOf2(length):
            return signal
        else:
            new_exp = int(math.log(length, 2)) + 1
            new_len = int(math.pow(2, new_exp))
            return signal + [0 for i in xrange(new_len - length)]

    @staticmethod
    def getImageRow(image, rowNumber):
        iHeight, iWidth = image.shape[0], image.shape[1]
        if rowNumber >= iHeight:
            print("Row " + str(rowNumber) + " should not be greater than height " + str(iHeight))
            return None
        return image[rowNumber, :].tolist()

    @staticmethod
    def get_angle(a, b):
        if b[0] - a[0] == 0:
            return 90.0
        return math.degrees(math.atan(float((b[1] - a[1])) / float((b[0] - a[0]))))

    @staticmethod
    def get_distance(a, b):
        return math.fabs(b[1] - a[1]) + math.fabs(b[0] + a[0])

    @staticmethod
    def draw_spikes(image, spikes, signal_row_number):
        for spike in spikes:
            print(spike)
            spike_start_position = (spike.getSigStartOfUpRun(), signal_row_number)
            spike_end_position = (spike.getSigStartOfUpRun() + spike.getSigLenOfUpRun(), signal_row_number)
            cv2.line(image, spike_start_position, spike_end_position, (0, 0, 255), 1)

            spike_start_position = (spike.getSigStartOfFlatRun(), signal_row_number)
            spike_end_position = (spike.getSigStartOfFlatRun() + spike.getSigLenOfFlatRun(), signal_row_number)
            cv2.line(image, spike_start_position, spike_end_position, (0, 255, 0), 1)

            spike_start_position = (spike.getSigStartOfDownRun(), signal_row_number)
            spike_end_position = (spike.getSigStartOfDownRun() + spike.getSigLenOfDownRun(), signal_row_number)
            cv2.line(image, spike_start_position, spike_end_position, (255, 0, 0), 1)

    @staticmethod
    def draw_lanes(image, points, angle_low_thresh, angle_high_thresh, color=(0, 0, 255), thickness=1):
        for i in xrange(0, len(points)-1):
            p = points[i]
            q = points[i+1]
            angle = NumUtils.get_angle(p, q)
            if angle_low_thresh <= angle <= angle_high_thresh:
                cv2.line(image, p, q, color, thickness)
            # else:
            #    cv2.line(image, p, q, (255, 255, 0), thickness)
			
	#Fits a stright line using 1d polyfit of scipy package

    @staticmethod
    def fit_lanes(image, points, angle_low_thresh, angle_high_thresh, color=(0, 0, 255), thickness=1):
        if len(points) <= 0:
            return
        x = [p[0] for p in points]
        y = [p[1] for p in points]
        # print("Num utils: X:" + str(x))
        # print("Num utils: Y:" + str(y))
        f = sp.poly1d(sp.polyfit(x, y, 1))

        start = (x[0], int(f(x[0])))
        end = (x[-1], int(f(x[-1])))
        # print("Num utils: start:" + str(start))
        # print("Num utils: end:" + str(end))
        angle = NumUtils.get_angle(start, end)
        if angle_low_thresh <= angle <= angle_high_thresh:
            cv2.line(image, start, end, color, thickness)

    @staticmethod
    def draw_line(image, lines, color, thickness=2):
        for line in lines:
            cv2.line(image, (line[0][0], line[0][1]), (line[1][0], line[1][1]), color, thickness)
        # for i in xrange(len(points) - 1):
        #    cv2.line(image, (int(points[i][0]), int(points[i][1])),
        #             (int(points[i + 1][0]), int(points[i + 1][1])), color, thickness)
