import cv2

#################################################
# module: OneDHWTLaneDetectorV2.py
# authors: Vladimir Kulyukin, Vikas Reddy
#################################################

from OneDHWT import OneDHWT
from OneDHWTSpikeDetector import OneDHWTSpikeDetector
from NumUtils import NumUtils
from Params import Params


class OneDHWTLaneDetectorV2:
    def __init__(self):
        pass

    # Retrieves specified sub row from 'start' to 'end'
    # Applies 1DHWT
    # returns the detected up-down spikes in HWT

    @staticmethod
    def get_up_down_spikes(row, start, end, num_of_iterations, signal_row_number):
        # print("OneDHWTLaneDetectorV2.get_up_down_spikes:\n start:" + str(start) + "\tend: " + str(end))
        row = row[start:end]
        row_hwt = row[:]
        OneDHWT.ordFHWTForNumIters(row_hwt, num_of_iterations)
        spikes = OneDHWTSpikeDetector. \
            detectUpDownSpikesInHWTOfRowSigSegmentByWaveDeg(row, row_hwt, num_of_iterations,
                                                            signal_row_number, start, end,
                                                            1.0, 1.0, 1, 1, 60.0, 60.0, )
        return spikes

    # Crops the ROI
    @staticmethod
    def crop_image(image):
        return image[Params.ROI_START_ROW:Params.ROI_END_ROW, Params.ROI_START_COL:Params.ROI_END_COL]

    # Can be improved by detecting the texture of road surface
    @staticmethod
    def pre_process(image, gaussian_kernel_size=(7, 7), gaussian_sigmaX=0,
                    threshold_type=cv2.THRESH_BINARY + cv2.THRESH_OTSU):
        temp = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        temp = cv2.GaussianBlur(temp, gaussian_kernel_size, gaussian_sigmaX)
        # temp = cv2.threshold(temp, threshold, 255, threshold_type)[1]
        # temp = cv2.adaptiveThreshold(temp, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        ret3, temp = cv2.threshold(temp, 0, 255, threshold_type)
        del image
        return temp

    # Input: Binary image (thresh)
    # Output: Left Lane Spike positions

    @staticmethod
    def get_ll_spike_positions(thresh, num_of_iterations=2, signal_row_start=235,
                               signal_row_end=120, signal_col_start=0, signal_col_end=64,
                               row_thresh=150, dbg=False, image=None):
        if dbg:
            print("     ########################## LEFT LANE ##########################     ")
        spike_positions = []
        no_spike_rows_count = 0
        for signal_row_number in xrange(signal_row_start, signal_row_end, -2):
            row = NumUtils.getImageRow(thresh, signal_row_number)
            ud_spikes = OneDHWTLaneDetectorV2.get_up_down_spikes(row, signal_col_start, signal_col_end,
                                                                 num_of_iterations, signal_row_number)

            # If no spikes gets detected the scan line rotated by 1 pixel,
            # the last (64th) pixel is the average of 62nd and 63rd pixels

            if len(ud_spikes) == 0:
                temp_row = row[1:]
                temp_row.append((temp_row[-1] + temp_row[-2])/2)
                ud_spikes = OneDHWTLaneDetectorV2.get_up_down_spikes(temp_row, signal_col_start,
                                                                     signal_col_end,
                                                                     num_of_iterations, signal_row_number)

            # If there are no spikes detected, incrementing the counter

            if len(ud_spikes) == 0:
                no_spike_rows_count += 1

            # If no spikes gets detected for consecutive 5 rows, then
            # scan line will be shifted by 7 pixels and tries to detect spikes

            if len(ud_spikes) == 0 and no_spike_rows_count >= 5:
                temp_signal_col_start = signal_col_start
                temp_signal_col_end = signal_col_end

                # The shifting continues until it reaches row_thresh

                while temp_signal_col_end < row_thresh:
                    temp_signal_col_start += 7
                    temp_signal_col_end += 7
                    row = NumUtils.getImageRow(thresh, signal_row_number)
                    ud_spikes = OneDHWTLaneDetectorV2.get_up_down_spikes(row, temp_signal_col_start,
                                                                         temp_signal_col_end,
                                                                         num_of_iterations, signal_row_number)
                    if len(ud_spikes) > 0:
                        signal_col_start = temp_signal_col_start
                        signal_col_end = temp_signal_col_end
                    # drawing buffer lines
                    if dbg:
                        cv2.line(image, (temp_signal_col_start, signal_row_number),
                                 (temp_signal_col_end, signal_row_number), (255, 0, 0), 1)

            if len(ud_spikes) > 0:
                no_spike_rows_count = 0
                if dbg:
                    print("LL: detected spikes: " + str(len(ud_spikes)))
                    for spike in ud_spikes:
                        print spike
                # Needs improvement
                spike_position = (OneDHWTLaneDetectorV2.optimum_spike_x(ud_spikes), signal_row_number)

                if dbg:
                    print("LL: Spike position: " + str(spike_position))
                '''
                spike_position = ((ud_spikes[0].getSigStartOfUpRun() + ud_spikes[0].getSigLenOfUpRun() / 2),
                                  signal_row_number)
                '''
                # setting previous spike position as mid point as the scan line

                delta = spike_position[0] - (signal_col_start + signal_col_end) / 2
                if delta > 0:
                    signal_col_start += delta
                    signal_col_end += delta
                spike_positions.append(spike_position)
            # drawing the scan lines
            if dbg:
                cv2.line(image, (signal_col_start, signal_row_number),
                         (signal_col_end, signal_row_number), (255, 255, 255), 1)
                print("LL: " + str(signal_row_number) + " , " + str(len(ud_spikes)))
                NumUtils.draw_spikes(image, ud_spikes, signal_row_number)
        return spike_positions

    # Input: Binary image (thresh)
    # Output: Left Lane Spike positions

    @staticmethod
    def get_rl_spike_positions(thresh, num_of_iterations=2, signal_row_start=235,
                               signal_row_end=120, signal_col_start=296, signal_col_end=360,
                               row_thresh=180, dbg=False, image=None):
        if dbg:
            print("     ########################## RIGHT LANE ##########################     ")
        spike_positions = []
        no_spike_rows_count = 0

        for signal_row_number in xrange(signal_row_start, signal_row_end, -2):
            row = NumUtils.getImageRow(thresh, signal_row_number)
            ud_spikes = OneDHWTLaneDetectorV2.get_up_down_spikes(row, signal_col_start, signal_col_end,
                                                                 num_of_iterations, signal_row_number)

            # If no spikes gets detected the scan line rotated by 1 pixel,
            # the last (64th) pixel is the average of 62nd and 63rd pixels

            if len(ud_spikes) == 0:
                temp_row = row[1:]
                temp_row.append((temp_row[-1] + temp_row[-2])/2)
                ud_spikes = OneDHWTLaneDetectorV2.get_up_down_spikes(temp_row, signal_col_start,
                                                                     signal_col_end,
                                                                     num_of_iterations, signal_row_number)

            # If there are no spikes detected, incrementing the counter

            if len(ud_spikes) == 0:
                no_spike_rows_count += 1

            # If no spikes gets detected for consecutive 5 rows, then
            # scan line will be shifted by 7 pixels and tries to detect spikes

            if len(ud_spikes) == 0 and no_spike_rows_count >= 5:
                temp_signal_col_start = signal_col_start
                temp_signal_col_end = signal_col_end

                # The shifting continues until it reaches row_thresh

                while temp_signal_col_start > row_thresh:
                    temp_signal_col_start -= 7
                    temp_signal_col_end -= 7
                    row = NumUtils.getImageRow(thresh, signal_row_number)
                    ud_spikes = OneDHWTLaneDetectorV2.get_up_down_spikes(row, temp_signal_col_start,
                                                                         temp_signal_col_end,
                                                                         num_of_iterations, signal_row_number)
                    if len(ud_spikes) > 0:
                        signal_col_start = temp_signal_col_start
                        signal_col_end = temp_signal_col_end
                    # drawing buffer lines
                    if dbg:
                        cv2.line(image, (temp_signal_col_start, signal_row_number),
                                 (temp_signal_col_end, signal_row_number), (255, 0, 0), 1)

            if len(ud_spikes) > 0:
                no_spike_rows_count = 0
                spike_position = (OneDHWTLaneDetectorV2.optimum_spike_x(ud_spikes), signal_row_number)
                '''
                spike_position = ((ud_spikes[0].getSigStartOfUpRun() + ud_spikes[0].getSigLenOfUpRun() / 2),
                                  signal_row_number)
                '''
                # setting previous spike position as mid point as the scan line
                delta = spike_position[0] - (signal_col_start + signal_col_end) / 2
                if delta < 0:
                    signal_col_start += delta
                    signal_col_end += delta
                spike_positions.append(spike_position)
            # drawing the scan lines
            if dbg:
                cv2.line(image, (signal_col_start, signal_row_number),
                         (signal_col_end, signal_row_number), (255, 255, 255), 1)
                print("LL: " + str(signal_row_number) + " , " + str(len(ud_spikes)))
                NumUtils.draw_spikes(image, ud_spikes, signal_row_number)
        return spike_positions

	#Filter lines based on angle
    @staticmethod
    def filter_lines(points, angle_low_thresh, angle_high_thresh, dbg=False):
        filtered_lines = []
        for i in xrange(0, len(points), 2):
            for j in xrange(i+1, len(points), 2):
                if dbg:
                    print("OneDHWTLaneDetectorV2.filter_points:" + str(i) + "\t" + str(j))
                angle = NumUtils.get_angle(points[i], points[j])
                if angle_low_thresh <= angle <= angle_high_thresh:
                    filtered_lines.append((points[i], points[j]))
                if dbg:
                    print("OneDHWTLaneDetectorV2.filter_points:\n" + str(points[i]) + "\t" + str(points[j]) +
                          "\tAngle: " + str(angle) + "\t" + str(angle_low_thresh <= angle <= angle_high_thresh))
        return filtered_lines

	#Filters cross points, 
    @staticmethod
    def filter_cross_points(ll_points, rl_points):
        if len(ll_points) < 2 or len(rl_points) < 2:
            return ll_points, rl_points
        filtered_ll_points = []
        filtered_rl_points = []
        sorted_ll_points = sorted(ll_points, key=lambda point: point[0])
        sorted_rl_points = sorted(rl_points, key=lambda point: point[0])
        for ll_point in ll_points:
            if ll_point[0] < sorted_rl_points[0][0]:
                filtered_ll_points.append(ll_point)
        for rl_point in rl_points:
            if rl_point[0] > sorted_ll_points[0][0]:
                filtered_rl_points.append(rl_point)
        return filtered_ll_points, filtered_rl_points

	#Calculate x co-ordinate of the optimum spike position by calculating the average of all the spikes.
    @staticmethod
    def optimum_spike_x(ud_spikes):
        numberOfSpikes = len(ud_spikes)
        if numberOfSpikes == 0:
            return None
        elif numberOfSpikes == 1:
            return OneDHWTLaneDetectorV2.get_spike_x(ud_spikes[0])
        else:
            # not sure what do
            sum_x = 0
            for spike in ud_spikes:
                sum_x += OneDHWTLaneDetectorV2.get_spike_x(spike)
            return sum_x/numberOfSpikes

	#returns x co-ordinate of the spike position
    @staticmethod
    def get_spike_x(spike):
        return spike.getSigStartOfFlatRun() + (spike.getSigLenOfFlatRun() / 2)
