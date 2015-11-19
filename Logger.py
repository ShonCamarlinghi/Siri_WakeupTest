import os, sys, time
import signal
import subprocess, shlex
from threading import Timer


total_t = 60
case = ['1test', '2test']
testSessionT = total_t * len(case)
outDir = '/Users/scamarlinghi/workspace/Siri_WakeupTest'
siriLog = os.path.join(outDir, 'siriLog.txt')
cmdB = 'idevicesyslog >> ' + siriLog + ' &'
#os.system(cmdB)



class Logger(object):
    def __init__(self, filename = 'Default.log'):
        self.terminal = sys.stdout
        self.log = open(filename, 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

def run(cmd, timeout_sec):
    proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    kill_proc = proc.kill()
    timer = Timer(timeout_sec, kill_proc, [proc])
    try:
        timer.start()
        stdout, stderr = proc.communicate()
    finally:
        timer.cancel()

run(cmdB, testSessionT)

def seraSera(value):
    fname = os.path.join(outDir, value + '.txt')
    print fname
    f = open(fname, 'a')
    #sys.stdout = Logger(f)
    start_t = time.asctime()
    start = time.time()
    f.write("\n=============================================================")
    f.write("\nCase: %s \nStart time: %s " % (value, start_t))
    f.write("\n=============================================================")
    cmd = 'tail -f /Users/scamarlinghi/workspace/Siri_WakeupTest/siriLog.txt >> '+ fname
    run(cmd, 60)
    #while True:
    #    delta_t = time.time() - start
    #    if delta_t >= total_t:
    #        break
    f.write("\n=============================================================")
    f.write("\nCase: %s \nEnd time: %s" % (value, time.asctime()))
    f.write("\n=============================================================")
    f.close()


def main():
    for value in case:
        seraSera(value)


if __name__ == '__main__':
    main()




