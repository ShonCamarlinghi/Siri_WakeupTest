#!/usr/bin/python
__author__ = 'scamarlinghi'


from subprocess import Popen
from threading import Timer
import time
case = [0, 1, 2]
cmd = 'ps'
#total_t=59

def run(cmd, value, t):
    start_t = time.asctime()
    start = time.time()
    print start_t
    start_t = time.asctime()
    start = time.time()
    p = Popen([cmd])
    print(value)
    print(p.pid)
    while True:
        delta_t = time.time() - start
        if delta_t >= t:
            break
    p.terminate()
    timer = Timer(1, p.kill)
    timer.start()
    p.wait()
    timer.cancel()  #
    print time.asctime()#  the child process exited



def main():
    for value in case:
        run(cmd,value, 5)

if __name__ == '__main__':
    main()

