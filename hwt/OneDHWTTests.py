import math
import copy
from NumUtils import NumUtils
from OneDHWT import OneDHWT

### Module: OneDHWTTests.py
### Author: vladimir kulyukin

class OneDHWTTests:

    @staticmethod
    def testOrdFHWT(signal):
        print("Original signal: %s" % str(signal))
        OneDHWT.ordFHWT(signal)
        print("Ord FHWT       : %s" % str(signal))

    @staticmethod
    def testOrdFHWTForNumIters(signal): 
        n = NumUtils.intLog2(len(signal))
        print("n = %d" % n)
        copy_signal = copy.deepcopy(signal)
        for i in xrange(1, n):
            print("num iters %d" % i)
            print("Original: %s" % str(signal))
            OneDHWT.ordFHWTForNumIters(signal, i)
            print("Transformed: %s" % str(signal))
            OneDHWT.orderedInvFHWTForNumIters(signal, i)
            print("Reversed: %s" % str(signal))
            for j in xrange(len(signal)):
                if signal[j] != copy_signal[j]: 
                     print("FALSE")
                     return
        print("TRUE")

    @staticmethod
    def testOrdInvFHWT(signal):
        n = NumUtils.intLog2(len(signal))
        orig_signal = copy.deepcopy(signal)
        print("n = %d" % n)
        print("signal: %s" % str(signal))
        OneDHWT.ordFHWT(signal)
        print("OneDHWT: %s" % str(signal))
        OneDHWT.ordInvFHWT(signal)
        print("OneInvDHWT: %s" % str(signal))
        rslt = NumUtils.areEqualLists(signal, orig_signal)
        print("signal equality: %s" % str(rslt))
        return rslt

    @staticmethod
    def testOrdInvFHWTForNumItersGivenNumFwdIters(signal, num_fwd_iters, num_inv_iters):
        if num_inv_iters > num_fwd_iters:
            raise Exception('num_inv_iters > num_fwd_iters')
        num_avail_iters = NumUtils.intLog2(len(signal))
        if num_inv_iters > num_avail_iters:
            raise Exception('num_inv_iters > num_avail_iters')
        orig_signal = copy.deepcopy(signal)
        sig_copy     = copy.deepcopy(signal)
        print("num_fwd_iters = %d" % num_fwd_iters)
        print("num_inv_iters  = %d" % num_inv_iters)
        OneDHWT.ordFHWTForNumIters(signal, num_fwd_iters)
        OneDHWT.ordFHWTForNumIters(sig_copy, num_fwd_iters - num_inv_iters) 
        OneDHWT.ordInvFHWTForNumItersGivenNumFwdIters(signal, num_fwd_iters, num_inv_iters)
        rslt = NumUtils.areEqualLists(signal, sig_copy)
        print(signal)
        print(sig_copy)
        print("signal equality: %s" % str(rslt))
        return rslt
        
    @staticmethod
    def ex_1_15_p10():
        signal = [9, 1]
        OneDHWTTests.testOrdFHWT(signal)

    @staticmethod
    def ex_1_3_2_4_p11(): 
        signal = [5, 1, 2, 8]
        OneDHWTTests.testOrdFHWT(signal)

    @staticmethod
    def ex_1_12_p19():
        signal = [3, 1, 0, 4, 8, 6, 9, 9]
        OneDHWTTests.testOrdFHWT(signal)
    
    @staticmethod
    def ex_1_16_p20(): 
        signal = [1, 7]
        OneDHWTTests.testOrdFHWT(signal)
     
    @staticmethod
    def ex_1_17_p21():
        signal = [2, 4, 8, 6]
        OneDHWTTests.testOrdFHWT(signal)

    @staticmethod 
    def ex_1_18_p21(): 
        signal = [5, 7, 3, 1]
        OneDHWTTests.testOrdFHWT(signal)

    @staticmethod 
    def ex_1_19_p21(): 
        signal = [8, 6, 7, 3, 1, 1, 2, 4]
        OneDHWTTests.testOrdFHWT(signal)
            
            
#OneDHWTTests.ex_1_15_p10()
#OneDHWTTests.ex_1_3_2_4_p11()            
#OneDHWTTests.ex_1_12_p19()
#OneDHWTTests.ex_1_16_p20()
#OneDHWTTests.ex_1_19_p21()
#OneDHWTTests.testOrdFHWTForNumIters([1, 7])

#OneDHWTTests.testOrdInvFHWT([8, 6, 7, 3, 1, 1, 2, 4])
#for i in xrange(20):
#   rslt = OneDHWTTests.testOrdInvFHWT(NumUtils.genListOfRandomInts(0, 200, 128))
#   if rslt == False:
#       break

OneDHWTTests.testOrdInvFHWTForNumItersGivenNumFwdIters([1, 2, 3, 4, 5, 6, 7, 8], 3, 1)
OneDHWTTests.testOrdInvFHWTForNumItersGivenNumFwdIters([1, 2, 3, 4, 5, 6, 7, 8], 3, 2)
OneDHWTTests.testOrdInvFHWTForNumItersGivenNumFwdIters([1, 2, 3, 4, 5, 6, 7, 8], 3, 3)

for i in xrange(20):
   for num_fwd_iters in xrange(1, 6):
        signal = NumUtils.genListOfRandomInts(0, 200, 32)
        for num_inv_iters in xrange(1, num_fwd_iters+1):
           rslt = OneDHWTTests.testOrdInvFHWTForNumItersGivenNumFwdIters(signal, num_fwd_iters,
                                                                   num_inv_iters)
           if rslt == False:
               break
