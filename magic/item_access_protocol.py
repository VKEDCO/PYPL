 Item Access Protocol
############ pickle_str_map.py ###########
##  *** Item Access Protocol example ***
##
##  Pickable map that maps basestring keys to
##  Python objects and implements the item
##  access protocol.

##
##  Python version: Python 2.7.1
##
##  Comments, bugs, and errors to
##  vladimir dot kulyukin at gmail dot com

##  http://www.youtube.com/user/vkedco                                                       
##########################################

__metaclass__ = type

import cPickle

class PickleStrMap:
    ## a Python dictionary is the only
    ## regular attribute of each instance.
    def __init__(self):
        self.__dict = {}

    ## a valid key must be an instance of
    ## basestring. If it is not, we'll
    ## raise a TypeError.
    ## Otherwise, we just return key.
    def __validateKey(self, key):
        if not isinstance(key, basestring):
            raise TypeError
        else:
            return key

    ## this method is called when len is called.
    def __len__(self):
        print '__len__ is called'
        return self.__dict.__len__()

    ## this method is called when [] is called.
    def __getitem__(self, key):
        print '__getitem__ is called'
        return self.__dict.get(key, None)

    ## this method is called when [] = is called.
    def __setitem__(self, key, value):
        print '__setitem__ is called'
        vk = self.__validateKey(key)
        self.__dict[vk] = value

    ## this method is called when del is called.
    def __delitem__(self, key):
        print '__delitem__ is called'
        del self.__dict[key]

    ## this is a decorator to define a static method.
    ## Since we will be unpickling from files, there is
    ## no need to have an object present and make this
    ## method bound.
    @staticmethod
    def load(picklefile):
        with open(picklefile, 'rb') as inpickle:
            return cPickle.load(inpickle)

    ## check to see if our map has this key.
    def hasKey(self, key):
        vk = self.__validateKey(key)
        return self.__dict.has_key(vk)

    ## pickle (serialize) the map into a file.
    def pickle(self, picklefile):
        with open(picklefile, 'wb') as infilehandle:
            cPickle.dump(self, infilehandle)

    ## this is for debugging only.
    ## displays the map as a sequence of
    ## key --> value lines.
    def display(self):
        for k, v in self.__dict.iteritems():
            print k, '-->', v

    ## get rid of all key value pairs in the
    ## map.
    def clear(self):
        self.__dict.clear()

## this is a simple test.
def test_00():
    sm = PickleStrMap() ## make a PickleStrMap object.
    sm['a'] = 1         ## 1+. calls __setitem__
    sm['b'] = 2         ## 2+. calls __setitem__
    print len(sm)       ## 3+. calls __len__
    del sm['a']         ## 4+. calls __delitem__
    print sm['b']       ## 5+. calls __getitem__
    sm['c'] = (1, 2)    ## 6. calls __setitem__
    sm.display()
    ## change this directory when you run
    ## it on your machine.
    pkl_file = 'd:/tmp/map.pkl'
    sm.pickle(pkl_file)
    print 'pickling done...'
    sm2 = PickleStrMap.load(pkl_file)
    print 'unpickling done...'
    sm2.display()
