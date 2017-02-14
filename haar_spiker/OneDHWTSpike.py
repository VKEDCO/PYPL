##########################
### Module: OneDHWTSpike.py
### Author: Vladimir Kulyukin
### 05Sept16 - initial implementation
##########################


class OneDHWTSpike:
    def __init__(self, up_wave_coeff_thresh=0, down_wave_coeff_thresh=0, num_iters=0,
                 wave_start_of_up_run=0, wave_len_of_up_run=0,
                 wave_start_of_flat_run=0, wave_len_of_flat_run=0,
                 wave_start_of_down_run=0, wave_len_of_down_run=0,
                 sig_row_or_col=0, sig_row_or_col_start=0, sig_row_or_col_end=0,
                 sig_start_of_up_run=0, sig_len_of_up_run=0,
                 sig_start_of_flat_run=0, sig_len_of_flat_run=0,
                 sig_start_of_down_run=0, sig_len_of_down_run=0):

        self.__mUpWaveCoeffThresh = up_wave_coeff_thresh
        self.__mDownWaveCoeffThresh = down_wave_coeff_thresh
        self.__mNumIters = num_iters

        self.__mWaveStartOfUpRun = wave_start_of_up_run
        self.__mWaveLenOfUpRun = wave_len_of_up_run

        self.__mWaveStartOfFlatRun = wave_start_of_flat_run
        self.__mWaveLenOfFlatRun = wave_len_of_flat_run

        self.__mWaveStartOfDownRun = wave_start_of_down_run
        self.__mWaveLenOfDownRun = wave_len_of_down_run

        self.__mSigRowOrCol = sig_row_or_col
        self.__mSigRowOrColStart = sig_row_or_col_start
        self.__mSigRowOrColEnd = sig_row_or_col_end

        self.__mSigStartOfUpRun = self.spikeWaveStartOfUpRunToSigPos(sig_row_or_col_start)
        self.__mSigLenOfUpRun = self.spikeWaveEndOfUpRunToSigPos(sig_row_or_col_start) - self.__mSigStartOfUpRun

        self.__mSigStartOfDownRun = self.spikeWaveStartOfDownRunToSigPos(sig_row_or_col_start)
        self.__mSigLenOfDownRun = self.spikeWaveEndOfDownRunToSigPos(sig_row_or_col_start) - self.__mSigStartOfDownRun

        self.__mSigStartOfFlatRun = self.__mSigStartOfUpRun + self.__mSigLenOfUpRun
        self.__mSigLenOfFlatRun = self.__mSigStartOfDownRun - self.__mSigStartOfFlatRun - 1

    def getUpWaveCoeffThresh(self):
        return self.__mUpWaveCoeffThresh

    def setUpWaveCoeffThresh(self, th):
        self.__mUpWaveCoeffThresh = th

    def getDownWaveCoeffThresh(self):
        return self.__mDownWaveCoeffThresh

    def setDownWaveCoeffThresh(self, th):
        self.__mDownWaveCoeffThresh = th

    def getNumIters(self):
        return self.__mNumIters

    def setNumIters(self, num_iters):
        self.__mNumIters = num_iters

    def getWaveStartOfUpRun(self):
        return self.__mWaveStartOfUpRun

    def setWaveStartOfUpRun(self, s):
        self.__mWaveStartOfUpRun = s

    def getWaveLenOfUpRun(self):
        return self.__mWaveLenOfUpRun

    def setWaveLenOfUpRun(self, ln):
        self.__mWaveLenOfUpRun = ln

    def getWaveStartOfFlatRun(self):
        return self.__mWaveStartOfFlatRun

    def setWaveStartOfFlatRun(self, s):
        self.__mWaveStartOfFlatRun = s

    def getWaveLenOfFlatRun(self):
        return self.__mWaveLenOfFlatRun

    def setWaveLenOfFlatRun(self, ln):
        self.__mWaveLenOfFlatRun = ln

    def getWaveStartOfDownRun(self):
        return self.__mWaveStartOfDownRun

    def setWaveStartOfDownRun(self, s):
        self.__mWaveStartOfDownRun = s

    def getWaveLenOfDownRun(self):
        return self.__mWaveLenOfDownRun

    def setWaveLenOfDownRun(self, ln):
        self.__mWaveLenOfDownRun = ln

    def getSigRowOrCol(self):
        return self.__mSigRowOrCol

    def setSigRowOrCol(self, r_or_c):
        self.__mSigRowOrCol = r_or_c

    def getSigRowOrColStart(self):
        return self.__mSigRowOrColStart

    def setSigRowOrColStart(self, r_or_c_start):
        self.__mSigRowOrColStart = r_or_c_start

    def getSigRowOrColEnd(self):
        return self.__mSigRowOrColEnd

    def setSigRowOrColEnd(self, r_or_c_end):
        self.__mSigRowOrColEnd = r_or_c_end

    def getSigStartOfUpRun(self):
        return self.__mSigStartOfUpRun

    def setSigStartOfUpRun(self, sig_start_of_up_run):
        self.__mSigStartOfUpRun = sig_start_of_up_run

    def getSigLenOfUpRun(self):
        return self.__mSigLenOfUpRun

    def setSigLenOfUpRun(self, sig_len_of_up_run):
        self.__mSigLenOfUpRun = sig_len_of_up_run

    def getSigStartOfFlatRun(self):
        return self.__mSigStartOfFlatRun

    def setSigStartOfFlatRun(self, sig_start_of_flat_run):
        self.__mSigStartOfFlatRun = sig_start_of_flat_run

    def getSigLenOfFlatRun(self):
        return self.__mSigLenOfFlatRun

    def setSigLenOfFlatRun(self, sig_len_of_flat_run):
        self.__mSigLenOfFlatRun = sig_len_of_flat_run

    def getSigStartOfDownRun(self):
        return self.__mSigStartOfDownRun

    def setSigStartOfDownRun(self, sig_start_of_down_run):
        self.__mSigStartOfDownRun = sig_start_of_down_run

    def getSigLenOfDownRun(self):
        return self.__mSigLenOfDownRun

    def setSigLenOfDownRun(self, sig_len_of_down_run):
        self.__mSigLenOfDownRun = sig_len_of_down_run

    ##Vikas, 22 Sep 2016
    def spikeWaveStartOfUpRunToSigPos(self, sig_start_pos):
        y = int(2 ** self.__mNumIters)
        return self.__mWaveStartOfUpRun * y + sig_start_pos

    def spikeWaveEndOfUpRunToSigPos(self, sig_start_pos):
        y = int(2 ** self.__mNumIters)
        return (self.__mWaveStartOfUpRun + self.__mWaveLenOfUpRun) * y + sig_start_pos

    def spikeWaveStartOfDownRunToSigPos(self, sig_start_pos):
        y = int(2 ** self.__mNumIters)
        return self.__mWaveStartOfDownRun * y + sig_start_pos

    def spikeWaveEndOfDownRunToSigPos(self, sig_start_pos):
        y = int(2 ** self.__mNumIters)
        return (self.__mWaveStartOfDownRun + self.__mWaveLenOfDownRun) * y + sig_start_pos

    def __str__(self):
        return 'Spike: r||c = ' + str(self.getSigRowOrCol()) + ', ' \
                                                               'sig_start =  ' + str(self.getSigRowOrColStart()) + ', ' \
                                                                                                                   'sig_end  =  ' + str(
            self.getSigRowOrColEnd()) + ', ' \
                                        'wu_start  =  ' + str(self.getWaveStartOfUpRun()) + ', ' \
                                                                                            'wu_len = ' + str(
            self.getWaveLenOfUpRun()) + ', ' \
                                        'wf_start = ' + str(self.getWaveStartOfFlatRun()) + ', ' \
                                                                                            'wf_len = ' + str(
            self.getWaveLenOfFlatRun()) + ', ' \
                                          'wd_start = ' + str(self.getWaveStartOfDownRun()) + ', ' \
                                                                                              'wd_len = ' + str(
            self.getWaveLenOfDownRun()) + ', ' \
                                          'su_start  =  ' + str(self.getSigStartOfUpRun()) + ', ' \
                                                                                             'su_len = ' + str(
            self.getSigLenOfUpRun()) + ', ' \
                                       'sf_start = ' + str(self.getSigStartOfFlatRun()) + ', ' \
                                                                                          'sf_len = ' + str(
            self.getSigLenOfFlatRun()) + ', ' \
                                         'sd_start = ' + str(self.getSigStartOfDownRun()) + ', ' \
                                                                                            'sd_len = ' + str(
            self.getSigLenOfDownRun())
