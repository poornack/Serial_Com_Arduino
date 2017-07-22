import time
import serial
import os

comPath = "/dev/tty.usbmodem1411"
comBaud_int = 9600
comBaud_str = "9600"

ardComm = serial.Serial(comPath, comBaud_int)

os.system("open SerialViewer.command")

def time_truncate(time, degree = 1):
    time_str = "{0:0.0f}".format(time)
    time_str_trunc = time_str[-degree:]
    return time_str_trunc
    
def num_to_LED(num, lastState):
    if num == "1" and lastState != 1:
        ardComm.write('1\n')
        print "CHANGED 1"
        lastState = 1
    elif num == "2" and lastState != 2:
        ardComm.write('2\n')
        print "CHANGED 2"
        lastState = 2
    elif num == "3" and lastState != 3:
        ardComm.write('1\n2\n')
        print "CHANGED 1 2"
        lastState = 3
    elif num == "4" and lastState != 4:
        ardComm.write('3\n')
        print "CHANGED 3"
        lastState = 4
    elif num == "5" and lastState != 5:
        ardComm.write('3\n1\n')
        print "CHANGED 1 3"
        lastState = 5
    elif num == "6" and lastState != 6:
        ardComm.write('3\n2\n')
        print "CHANGED 2 3"
        lastState = 6
    elif num == "7" and lastState != 7:
        ardComm.write('1\n2\n3\n')
        print "CHANGED 1 2 3"
        lastState = 7
    
    return lastState
        
lastState = 0;
    
while 1:
    t0 = time.time()
    t0_trunc = time_truncate(t0)
    #print t0_trunc
    lastState = num_to_LED(t0_trunc, lastState)