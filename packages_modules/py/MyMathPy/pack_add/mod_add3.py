import mod_constants

def add3(x, y, z): return x + y + z

## function that prints module's info.
def info():
    print 'This is mod_add3 module of ', \
          mod_constants.app_name, \
          ' version ', mod_constants.version
