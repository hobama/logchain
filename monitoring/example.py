# import sys, threading, time, queue
# from pyqt5 import qtwidgets
# from monitoring import form
import time

if __name__ == '__main__':
    t = time.time()
    localtime = time.localtime(t)
    print(localtime)
    mktime = time.mktime(localtime)
    local = int(round(mktime*1000.0))
    print(str(local))
