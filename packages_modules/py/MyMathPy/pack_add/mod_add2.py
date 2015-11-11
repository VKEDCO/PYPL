import mod_constants

def add2(x, y): return x + y

## function that prints module's info.
def info():
    print 'This is mod_add2 module of ', \
          mod_constants.app_name, ' application ',\
          ' version ', mod_constants.version
