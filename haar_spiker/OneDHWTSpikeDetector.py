##################################
## module: OneDHWTSpikeDetector.py
## author: vladimir kulyukin
##################################

from __future__ import division

import math

from OneDHWTSpike import OneDHWTSpike


class OneDHWTSpikeDetector:
    @staticmethod
    def isSpikeStrongEnoughByWaveDeg(spike, hwt,
                                     up_deg_angle_thresh, down_deg_angle_thresh):
        up_start_col = spike.getWaveStartOfUpRun()
        up_end_col = up_start_col + spike.getWaveLenOfUpRun() - 1

        up_x = (up_end_col - up_start_col + 1) * 2
        up_y = abs(hwt[up_end_col] - hwt[up_start_col])
        up_deg = math.atan2(up_y, up_x) * (180 / math.pi)

        down_start_col = spike.getWaveStartOfDownRun()
        down_end_col = down_start_col + spike.getWaveLenOfDownRun() - 1

        down_x = (down_end_col - down_start_col + 1) * 2
        down_y = abs(hwt[down_end_col] - hwt[down_start_col])
        down_deg = math.atan2(down_y, down_x) * (180 / math.pi)

        return up_deg >= up_deg_angle_thresh and down_deg >= down_deg_angle_thresh

    @staticmethod
    def detectUpDownSpikesInHWTOfRowSigSegmentByWaveDeg(row_sig_segment,
                                                        hwt, num_iters,
                                                        sig_row, sig_col_start, sig_col_end,
                                                        uwc_thresh, dwc_thresh,
                                                        up_run_len_thresh, down_run_len_thresh,
                                                        up_deg_angle_thresh, down_deg_angle_thresh,
                                                        add_weak_spikes=True):
        dbg = False
        spikes = []

        hwt_size = int(len(hwt) / (2 ** num_iters))
        # print 'detectUpDownSpikesInHWTOfRowSigSegmentByWaveDeg: HWT_SIZE', hwt_size

        n = 2 * hwt_size
        i = hwt_size

        up_run_start = -1
        down_run_start = -1
        flat_run_start = -1

        while i < n:
            if dbg:
                print("i = %d" % i)
            j = i
            up_run_start = j
            while j < n:
                if dbg:
                    print "hwt[", j, "]=", str(hwt[j])
                if hwt[j] >= 0:
                    if dbg:
                        print "breaking out of up-loop at", str(j), "hwt[j]>=0"
                    break

                if abs(hwt[j]) < uwc_thresh:
                    if dbg:
                        print "breaking out of up-loop at", str(j), "abs(hwt[j])<uwc_thresh"
                    break

                j += 1

            up_run_len = j - up_run_start
            if dbg:
                print "up_run_len=", str(up_run_len)
            if up_run_len < up_run_len_thresh:
                up_run_start = -1
                down_run_start = -1
                i += 1
                continue

            flat_run_start = j
            while j < n:
                if abs(hwt[j]) >= uwc_thresh or abs(hwt[j]) >= dwc_thresh:
                    if dbg:
                        print "breaking out of flat-loop at", str(j), "|hwt[j]| >= u/dwc_thresh"
                    break
                j += 1
            flat_run_len = j - flat_run_start
            if dbg:
                print "starting flat run at", str(j)
            if flat_run_len <= 0:
                flat_run_start = -1

            if j + down_run_len_thresh - 1 >= n:
                up_run_start = -1
                down_run_start = -1
                if dbg:
                    print "j + down_run_len_thresh >= n"
                    print "no more spikes"
                break

            down_run_start = j
            while j < n:
                if hwt[j] <= 0:
                    if dbg:
                        print "breaking out of down-loop at", str(j), "hwt[j]<=0"
                    break
                if hwt[j] < dwc_thresh:
                    if dbg:
                        print "breaking out of down-loop at", str(j), "hwt[j]<dwc_thresh"
                    break
                j += 1

            down_run_len = j - down_run_start

            if down_run_len < down_run_len_thresh:
                if dbg:
                    print "continuing because down_run_len < down_run_len_thresh"
                up_run_start = -1
                down_run_start = -1
                i += 1
                continue

            spike = None

            if flat_run_len > 0:
                spike = OneDHWTSpike(
                    up_wave_coeff_thresh=uwc_thresh,
                    down_wave_coeff_thresh=dwc_thresh,
                    num_iters=num_iters,
                    wave_start_of_up_run=up_run_start - hwt_size,
                    wave_len_of_up_run=up_run_len,
                    wave_start_of_flat_run=flat_run_start - hwt_size,
                    wave_len_of_flat_run=flat_run_len,
                    wave_start_of_down_run=down_run_start - hwt_size,
                    wave_len_of_down_run=down_run_len,
                    sig_row_or_col=sig_row,
                    sig_row_or_col_start=sig_col_start,
                    sig_row_or_col_end=sig_col_end)
            else:
                spike = OneDHWTSpike(
                    up_wave_coeff_thresh=uwc_thresh,
                    down_wave_coeff_thresh=dwc_thresh,
                    num_iters=num_iters,
                    wave_start_of_up_run=up_run_start - hwt_size,
                    wave_len_of_up_run=up_run_len,
                    wave_start_of_down_run=down_run_start - hwt_size,
                    wave_len_of_down_run=down_run_len,
                    sig_row_or_col=sig_row,
                    sig_row_or_col_start=sig_col_start,
                    sig_row_or_col_end=sig_col_end)

            if OneDHWTSpikeDetector.isSpikeStrongEnoughByWaveDeg(spike, hwt,
                                                                 up_deg_angle_thresh,
                                                                 down_deg_angle_thresh):
                if dbg:
                    print "Detected a strong spike by wave deg"
                spikes.append(spike)
            elif add_weak_spikes == True:
                spikes.append(spike)
                if dbg:
                    print 'Detected a weak spike by wave deg'

            i = j + 1

        return spikes

    @staticmethod
    def detectDownUpSpikesInHWTOfRowSigSegmentByWaveDeg(row_sig_segment,
                                                        hwt, num_iters,
                                                        sig_row, sig_col_start, sig_col_end,
                                                        uwc_thresh, dwc_thresh,
                                                        up_run_len_thresh, down_run_len_thresh,
                                                        up_deg_angle_thresh, down_deg_angle_thresh,
                                                        add_weak_spikes=True):
        spikes = []
        hwt_size = int(len(hwt) / (2 ** num_iters))
        print("detectDownUpSpikesInHWTOfRowSigSegmentByWaveDeg HWT_SIZE: " + str(hwt_size))
        n = 2 * hwt_size
        i = hwt_size

        up_run_start = -1
        down_run_start = -1
        flat_run_start = -1

        while i < n:
            j = i
            down_run_start = j
            while j < n:
                if hwt[j] <= 0:
                    break

                if abs(hwt[j]) < dwc_thresh:
                    break

                j += 1

            down_run_len = j - down_run_start
            if down_run_len < down_run_len_thresh:
                down_run_start = -1
                up_run_start = -1
                i += 1
                continue

            flat_run_start = j
            while j < n:
                if abs(hwt[j]) >= uwc_thresh or abs(hwt[j]) >= dwc_thresh:
                    break
                j += 1

            flat_run_len = j - flat_run_start
            if flat_run_len <= 0:
                flat_run_start = -1

            if j + up_run_len_thresh - 1 >= n:
                up_run_start = -1
                down_run_start = -1
                break

            up_run_start = j
            while j < n:
                if hwt[j] >= 0:
                    break
                if hwt[j] < uwc_thresh:
                    break

                j += 1

            up_run_len = j - up_run_start

            if up_run_len < up_run_len_thresh:
                up_run_start = -1
                down_run_start = -1
                i += 1
                continue

            spike = None

            if flat_run_len > 0:
                spike = OneDHWTSpike(
                    up_wave_coeff_thresh=uwc_thresh,
                    down_wave_coeff_thresh=dwc_thresh,
                    num_iters=num_iters,
                    wave_start_of_up_run=up_run_start - hwt_size,
                    wave_len_of_up_run=up_run_len,
                    wave_start_of_flat_run=flat_run_start - hwt_size,
                    wave_len_of_flat_run=flat_run_len,
                    wave_start_of_down_run=down_run_start - hwt_size,
                    wave_len_of_down_run=down_run_len,
                    sig_row_or_col=sig_row,
                    sig_row_or_col_start=sig_col_start,
                    sig_row_or_col_end=sig_col_end)
            else:
                spike = OneDHWTSpike(
                    up_wave_coeff_thresh=uwc_thresh,
                    down_wave_coeff_thresh=dwc_thresh,
                    num_iters=num_iters,
                    wave_start_of_up_run=up_run_start - hwt_size,
                    wave_len_of_up_run=up_run_len,
                    wave_start_of_down_run=down_run_start - hwt_size,
                    wave_len_of_down_run=down_run_len)

            if OneDHWTSpikeDetector.isSpikeStrongEnoughByWaveDeg(spike,
                                                                 hwt,
                                                                 up_deg_angle_thresh,
                                                                 down_deg_angle_thresh):
                spikes.append(spike)
            elif add_weak_spikes == True:
                spikes.append(spike)

            i = j + 1

        return spikes

    @staticmethod
    def isObjPresent(gimg, hl_count_thresh=1, hl_lower_magn_thresh=5,
                     hl_upper_magn_thresh=15):
        try:
            pass
        except Exception as ex:
            print("ObjHWTDetector.isObjPresent exception: %s" % str(ex))
