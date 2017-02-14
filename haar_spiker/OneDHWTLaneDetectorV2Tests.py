import argparse
import sys
import traceback
from datetime import datetime
from os import listdir
import cv2

import time
import numpy
from NumUtils import NumUtils
from Params import Params
from OneDHWTLaneDetectorV2 import OneDHWTLaneDetectorV2
import warnings
warnings.simplefilter('ignore', numpy.RankWarning)

#####################################################
# module: OneDHWTLaneDetectorV2Tests.py
# author: Vikas Reddy
#####################################################

def unit_test01():
    global debug
    debug = True
    ## change these directories
    run("/home/vikas/Desktop/Research/JeepPix/12oct2016/16_07_02_14_43_41_orig.png",
        "/home/vikas/Desktop/test4.png")

# This code processes single image and returns the output image

def process_image(image):
    image2 = image[:]
    image = OneDHWTLaneDetectorV2.crop_image(image)

    thresh = OneDHWTLaneDetectorV2.pre_process(image)

    ll_points = OneDHWTLaneDetectorV2.get_ll_spike_positions(thresh,
                                                             signal_row_start=Params.ROI_HEIGHT - 1, signal_row_end=0,
                                                             signal_col_start=0, signal_col_end=64,
                                                             row_thresh=40)

    rl_points = OneDHWTLaneDetectorV2.get_rl_spike_positions(thresh,
                                                             signal_row_start=Params.ROI_HEIGHT - 1, signal_row_end=0,
                                                             signal_col_start=(Params.ROI_WIDTH - 64),
                                                             signal_col_end=Params.ROI_WIDTH,
                                                             row_thresh=40)

    ll_points, rl_points = OneDHWTLaneDetectorV2.filter_cross_points(ll_points, rl_points)

    updated_ll_points = [tuple((a + Params.ROI_START_COL, b + Params.ROI_START_ROW)) for a, b in ll_points]
    updated_rl_points = [tuple((a + Params.ROI_START_COL, b + Params.ROI_START_ROW)) for a, b in rl_points]

    NumUtils.draw_lanes(image2, updated_ll_points, -60, -30, color=(0, 255, 0), thickness=2)
    NumUtils.draw_lanes(image2, updated_rl_points, 30, 60, color=(0, 0, 255), thickness=2)

    cv2.rectangle(image2, (Params.ROI_START_COL, Params.ROI_START_ROW), (Params.ROI_END_COL, Params.ROI_END_ROW),
                  (255, 255, 0))

    return image2

# This code processes single image given in image_path and saves the processed
# image in the output_path

def run(image_path, output_path):
    image = cv2.imread(image_path)
    image2 = image[:]
    image = OneDHWTLaneDetectorV2.crop_image(image)
    thresh = OneDHWTLaneDetectorV2.pre_process(image)
    row_thresh = int(image.shape[1]/2)

    ll_points = OneDHWTLaneDetectorV2.get_ll_spike_positions(thresh,
                                                             signal_row_start=Params.ROI_HEIGHT - 1, signal_row_end=0,
                                                             signal_col_start=0, signal_col_end=64,
                                                             dbg=debug, row_thresh=row_thresh, image=image2)

    rl_points = OneDHWTLaneDetectorV2.get_rl_spike_positions(thresh,
                                                             signal_row_start=Params.ROI_HEIGHT - 1, signal_row_end=0,
                                                             signal_col_start=(Params.ROI_WIDTH - 64),
                                                             signal_col_end=Params.ROI_WIDTH,
                                                             dbg=debug, row_thresh=row_thresh, image=image2)

    ll_points, rl_points = OneDHWTLaneDetectorV2.filter_cross_points(ll_points, rl_points)

    # filtered_ll_points = OneDHWTLaneDetectorV2.filter_lines(ll_points, -60, -30, dbg=debug)
    # filtered_rl_points = OneDHWTLaneDetectorV2.filter_lines(rl_points, 30, 60, dbg=debug)

    updated_ll_points = [tuple((a + Params.ROI_START_COL, b + Params.ROI_START_ROW)) for a, b in ll_points]
    updated_rl_points = [tuple((a + Params.ROI_START_COL, b + Params.ROI_START_ROW)) for a, b in rl_points]

    if debug:
        print("Filtered ll points: " + str(ll_points))
        print("Filtered rl points: " + str(rl_points))
        print("Updated ll points: " + str(updated_ll_points))
        print("Updated rl points: " + str(updated_rl_points))

    # NumUtils.draw_line(image2, updated_ll_points, (0, 255, 0))
    # NumUtils.draw_line(image2, updated_rl_points, (0, 0, 255))

    # NumUtils.draw_line(image2, filtered_ll_points, (0, 255, 0))
    # NumUtils.draw_line(image2, filtered_rl_points, (0, 0, 255))

    # NumUtils.draw_lanes(image, ll_points, -60, -30, color=(0, 255, 0), thickness=2)
    # NumUtils.draw_lanes(image, rl_points, 30, 60, color=(0, 0, 255), thickness=2)

    # NumUtils.draw_lanes(image2, updated_ll_points, -60, -30, color=(0, 255, 0), thickness=2)
    # NumUtils.draw_lanes(image2, updated_rl_points, 30, 60, color=(0, 0, 255), thickness=2)

    NumUtils.fit_lanes(image2, updated_ll_points, -60, -30, color=(0, 255, 0), thickness=2)
    NumUtils.fit_lanes(image2, updated_rl_points, 30, 60, color=(0, 0, 255), thickness=2)

    cv2.rectangle(image2, (Params.ROI_START_COL, Params.ROI_START_ROW), (Params.ROI_END_COL, Params.ROI_END_ROW), (255, 255, 0))
    cv2.imwrite(output_path, image2)

    del image2
    del image
    del thresh
    del ll_points
    del rl_points
    # del filtered_ll_points
    # del filtered_rl_points

# This function processes all the images in a directory and
# saves the output images in the output directory

def run_for_dir():
    start = datetime.now()
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--input_dir', required=True,
                    help='path to input images directory')
    ap.add_argument('-o', '--output_dir', required=True,
                    help='path to output images directory')

    args = vars(ap.parse_args())

    input_dir = args['input_dir']
    output_dir = args['output_dir']

    imageFiles = listdir(input_dir)
    total_count = float(len(imageFiles))
    count = 1

    for imageFile in imageFiles:
        try:
            sys.stdout.write('\r')
            progress = (count / total_count) * 100
            sys.stdout.write("Progress: %.2f%%" % progress)
            sys.stdout.flush()
            count += 1
            run(input_dir + imageFile, output_dir + imageFile)
        except Exception as e:
            print("\tException " + e.message + "\t" + imageFile + "\n")
            traceback.print_exc(file=sys.stdout)
            print
    end = datetime.now()
    total_time = (end - start).total_seconds()
    frame_rate = total_count / total_time
    print("\nTotal time for " + str(int(total_count)) + " images is " + str(total_time))
    print("Frame rate: " + str(frame_rate))

# This code captures images from Raspberry Pi Camera, processes, and then
# displays on the touch screen display
'''
from picamera.array import PiRGBArray
from picamera import PiCamera


def run_for_camera():
    camera = PiCamera()
    camera.resolution = (368, 240)
    camera.framerate = 20
    rawCapture = PiRGBArray(camera, size=(368, 240))
    cv2.namedWindow("Lane detection")
    cv2.setWindowProperty("Lane detection", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # cv2.resizeWindow("Lane detection", 720, 400)
    time.sleep(0.2)

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        frame = frame.array

        output = process_image(frame)
        cv2.imshow("Lane detection", output)
        rawCapture.truncate(0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        del frame
        del output

    cv2.destroyAllWindows()
'''

# Execution starts here
if __name__ == '__main__':
    debug = False
    # unit_test01()
    run_for_dir()
