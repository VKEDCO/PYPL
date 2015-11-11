import mod_constants

def mult4(x, y, z, w): return x * y * z * w

## function that prints module's info.
def info():
    print 'This is mod_mult4 module of ', \
          mod_constants.app_name, ' application '\
          ' version ', mod_constants.version
