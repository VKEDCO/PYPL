import math

from NumUtils import NumUtils

###################################
### Module: OneDHWT.py
### Author: Vladimir Kulyukin
###################################

class OneDHWT:
    @staticmethod
    def ordFHWT(signal):
        sig_len = len(signal)
        if not NumUtils.isPowOf2(sig_len):
            raise Exception('sig_len is not PowOf2')
        num_sweeps = NumUtils.intLog2(sig_len)
        if num_sweeps == 1:
            acoeff = (signal[0] + signal[1]) / 2.0
            ccoeff = (signal[0] - signal[1]) / 2.0
            signal[0] = acoeff
            signal[1] = ccoeff
            return
        acoeffs = []
        ccoeffs = []
        for sweep_num in xrange(1, num_sweeps):
            size = int(math.pow(2, num_sweeps - sweep_num))
            ## print("size = %d" % size)
            acoeffs = [0.0 for i in xrange(size)]
            ccoeffs = [0.0 for i in xrange(size)]
            ai = 0
            ci = 0
            end = int(math.pow(2, num_sweeps - sweep_num + 1)) - 1
            for i in xrange(0, end + 1, 2):
                acoeffs[ai] = (signal[i] + signal[i + 1]) / 2.0
                ccoeffs[ci] = (signal[i] - signal[i + 1]) / 2.0
                ai += 1
                ci += 1
            for i in xrange(0, size):
                signal[i] = acoeffs[i]
                signal[i + size] = ccoeffs[i]

        acoeff = (signal[0] + signal[1]) / 2.0
        ccoeff = (signal[0] - signal[1]) / 2.0
        signal[0] = acoeff
        signal[1] = ccoeff

    @staticmethod
    def ordFHWTForNumIters(signal, num_iters):
        sig_len = len(signal)
        if not NumUtils.isPowOf2(sig_len):
            return
        num_sweeps = NumUtils.intLog2(sig_len)
        if num_iters > num_sweeps:
            raise Exception('ordFHWTForNumIters: num_iters > num_sweeps')
        acoeff = 0
        ccoeff = 0
        if num_sweeps == 1:
            acoeff = (signal[0] + signal[1]) / 2.0
            ccoeff = (signal[0] - signal[1]) / 2.0
            signal[0] = acoeff
            signal[1] = ccoeff
            return
        acoeffs = []
        ccoeffs = []
        for sweep_num in xrange(1, num_iters + 1):
            size = int(math.pow(2, num_sweeps - sweep_num))
            acoeffs = [0.0 for i in xrange(size)]
            ccoeffs = [0.0 for i in xrange(size)]
            ai = 0
            ci = 0
            end = int(math.pow(2.0, num_sweeps - sweep_num + 1)) - 1
            for i in xrange(0, end + 1, 2):
                acoeffs[ai] = (signal[i] + signal[i + 1]) / 2.0
                ccoeffs[ci] = (signal[i] - signal[i + 1]) / 2.0
                ai += 1
                ci += 1
            for i in xrange(size):
                signal[i] = acoeffs[i]
                signal[i + size] = ccoeffs[i]

    ## ordered inverse fast HWT
    @staticmethod
    def ordInvFHWT(signal):
        sig_len = len(signal)
        if sig_len < 2 or not NumUtils.isPowOf2(sig_len):
            raise Exception('sig_len < 2 or not isPowOf2')
        num_iters = NumUtils.intLog2(sig_len)
        a0 = 0
        a1 = 0
        restored_vals = None
        gap = 0
        for scale in xrange(1, num_iters + 1):
            gap = int(math.pow(2, scale - 1))
            restored_vals = []
            restored_vals = [0.0 for i in xrange(2 * gap)]
            for i in xrange(gap):
                a0 = signal[i] + signal[gap + i]
                a1 = signal[i] - signal[gap + i]
                restored_vals[2 * i] = a0
                restored_vals[2 * i + 1] = a1
            for i in xrange(2 * gap):
                signal[i] = restored_vals[i]

    ## this method assumes that all iterations
    ## of ordered HWT have been applied to signal
    @staticmethod
    def ordInvFHWTForNumIters(signal, num_iters):
        sig_len = len(signal)
        if sig_len < 2 or not NumUtils.isPowOf2(sig_len):
            return
        num_avail_iters = NumUtils.intLog2(sig_len)
        if num_iters > num_avail_iters:
            return
        a0, a1 = 0, 0
        restored_vals = None
        gap = 1
        j = 0
        for scale in xrange(1, num_iters + 1):
            restored_vals = []
            restored_vals = [0 for i in xrange(2 * gap)]
            for i in xrange(gap):
                a0 = signal[i] + signal[gap + i]
                a1 = signal[i] - signal[gap + i]
                restored_vals[2 * i] = a0
                restored_vals[2 * i + 1] = a1
            for i in xrange(2 * gap):
                signal[i] = restored_vals[i]
            gap *= 2

    ## this method assumes that ordered FHWT has been applied to signal
    ## for num_fwd_iters
    @staticmethod
    def ordInvFHWTForNumItersGivenNumFwdIters(signal, num_fwd_iters, num_inv_iters):
        print("num_fwd_iters = %d" % num_fwd_iters)
        print("num_inv_iters = %d" % num_inv_iters)
        sig_len = len(signal)
        if sig_len < 2 or not NumUtils.isPowOf2(sig_len):
            raise Exception('sig_len < 2 or not isPowOf2')
        num_avail_iters = NumUtils.intLog2(sig_len)
        if num_inv_iters > num_fwd_iters:
            raise Exception('ordInvFHWTForNumItersGivenNumFwdIters: num_inv_iters > num_fwd_iters')
        a0, a1 = 0, 0
        restored_vals = None
        gap = int(math.pow(2, num_avail_iters - num_fwd_iters))
        print "num_avail_iters", str(num_avail_iters)
        print "num_fwd_iters", str(num_fwd_iters)
        print "gap", str(gap)
        j = 0
        for scale in xrange(1, num_inv_iters + 1):
            restored_vals = []
            restored_vals = [0 for i in xrange(2 * gap)]
            for i in xrange(gap):
                a0 = signal[i] + signal[gap + i]
                a1 = signal[i] - signal[gap + i]
                restored_vals[2 * i] = a0
                restored_vals[2 * i + 1] = a1
            for i in xrange(2 * gap):
                signal[i] = restored_vals[i]
            gap *= 2
