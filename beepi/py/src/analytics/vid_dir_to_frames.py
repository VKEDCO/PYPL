###########################################################################
# USAGE
# python vid_dir_to_frames.py -vd input_dir/vids/ -fd output_dir/traj/
# For each video vid.mp4 in input_dir/vids a subdirectory output_dir/traj/vid/
# is created and all frames from input_dir/vids/vid.mp4 are saved
# in output_dir/traj/vid/ and enumerated. For example, if vid4.mp4 contains
# 5 frames, then output_dir/traj/vid/ will contain
# output_dir/traj/vid/vid_0.png
# output_dir/traj/vid/vid_1.png
# output_dir/traj/vid/vid_2.png
# output_dir/traj/vid/vid_3.png
# output_dir/traj/vid/vid_4.png
#
# author: vladimir kulyukin
###########################################################################

import numpy as np
import argparse
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-vd', '--vd', help='path to video directory', required=True)
ap.add_argument('-fd', '--fd', help='path to the dir where frames are saved',
                required=True)

args = vars(ap.parse_args())

def createFrameDirAndFilename(vid_path, frame_dir):
    #print 'create_frame_dir_and_filename', vid_path, frame_dir
    h, t = os.path.split(vid_path)
    dir_name = t.split('.')[0]
    if frame_dir[-1] == '/':
        return frame_dir + dir_name + '/', dir_name 
    else:
        return frame_dir + '/' + dir_name + '/', dir_name

def getBaseDirName(dirpath):
    path = os.path.normpath(dirpath)
    return path.split(os.sep)[-1]

def getHourMinSec(baseDirName):
    underscoreSplits = baseDirName.split('_')
    lastElem = underscoreSplits[-1].split('.')[0]
    hyphenSplits = lastElem.split('-')
    return int(hyphenSplits[0]), int(hyphenSplits[1]), int(hyphenSplits[2])

def createMinPred(minutes):
    def minPred(dirpath):
        print dirpath
        return getHourMinSec(getBaseDirName(dirpath))[1] == minutes
    return minPred

def splitVideoIntoFrames(vid_path, frame_dir, frame_filename):
    print vid_path, frame_dir, frame_filename
    if not os.path.exists(frame_dir):
        os.makedirs(frame_dir)

    frame_counter = 0

    camera = cv2.VideoCapture(vid_path)
    # keep looping  
    while True:
        # grab the current frame
        (grabbed, frame) = camera.read()

        # if we are viewing a video and we did not grab a frame,
        # then we have reached the end of the video
        if not grabbed:
            break

        fc = frame.copy()
        print frame_dir + frame_filename + '_' + str(frame_counter) + '.png'
        cv2.imwrite(frame_dir + frame_filename + '_' + str(frame_counter) + '.png', fc)
        #pf = process_frame(frame, fc)
        #cv2.imwrite(frame_dir + "frp_" + str(frame_counter) + ".png", pf)
        #cv2.imshow('Current Frame', fc)
        frame_counter += 1
        key = cv2.waitKey(1) & 0xFF
        # if the 'q' key is pressed, stop the loop
        if key == ord('q'):
            break
        
    camera.release()

def splitVidDirIntoFrames(vid_dir, frame_dir, filePred):
    for vid_path in [os.path.join(vid_dir, vf) for vf in os.listdir(vid_dir) if os.path.isfile(os.path.join(vid_dir, vf))]:
        #print 'vid_path=', vid_path
        if filePred(vid_path):
            fd, fn = createFrameDirAndFilename(vid_path, frame_dir)
            #print 'fd=', fd
            #print 'fn=', fn
            splitVideoIntoFrames(vid_path, fd, fn)

if __name__ == '__main__':
    vid_dir = args['vd']
    frame_dir = args['fd']
    splitVidDirIntoFrames(vid_dir, frame_dir, lambda x: True)

# cleanup the camera and close any open windows
#camera.release()
#cv2.destroyAllWindows()
