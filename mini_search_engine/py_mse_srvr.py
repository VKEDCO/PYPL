from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler
import rtrvr

srvr_dir    = '/home/vladimir/code/python/mse/'
docmap      = 'file_to_docset_map.pkl'
punct_marks = ' `~!@#$%%^&*()_+{}|\[];\':";\',./?><'
stoplist    = 'stoplist.pkl'

## Since this is a forking server, the rtrvr object
## is constructed anew in each forked process.
rtrvr = rtrvr.TextRtrvr(docset_map_file = srvr_dir + docmap,
                        punctuation_marks = punct_marks,
                        stoplist_file = srvr_dir + stoplist)

class PyMSEServer(ForkingMixIn, TCPServer):
    pass

class PyMSERequestHandler(StreamRequestHandler):

    def __processData(self):
        global rtrvr
        print 'Processing: ' + self.query + "\n";
        try:
            return rtrvr.cgiMatchQuery(self.query)
        except Exception, e:
            return e
           
    def handle(self):
        self.addr = self.request.getpeername()
        self.query = self.rfile.readline().strip()
        print 'Query: ' + str(self.addr) + ' ' + str(self.query) + "\n";
        self.wfile.write(str(self.__processData()))
        self.wfile.flush()

my_mse_srvr = PyMSEServer(('', 1123), PyMSERequestHandler)
print 'PyMSEServer serving on ' + str(my_mse_srvr.server_address) + "\n"
my_mse_srvr.serve_forever()
