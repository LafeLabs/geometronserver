#!/usr/bin/env python
import serial
import math
import datetime
#python -m serial.tools.list_ports to find port, '/dev/cu.usbmodemFD111' on mac laptop
ser = serial.Serial('/dev/ttyACM0')  # open serial port

s = ser.readlines(100)
ssum = 0 
for index in range(len(s)):
    if s[index].rstrip().lstrip() != '':
        ssum += int(s[index].rstrip().lstrip())
savg = ssum/len(s)
svar = 0
for index in range(len(s)):
    if s[index].rstrip().lstrip() != '':
        svar += (int(s[index].rstrip().lstrip()) - savg)**2
svar /= len(s)**2
sigma = math.sqrt(svar)
ser.close()
datestring = ""
dateobject = datetime.datetime.now()
datestring = str(dateobject.year) + "_" + str(dateobject.month) + "_" + str(dateobject.day) + "_" + str(dateobject.hour) + "_" + str(dateobject.minute)+ "_" + str(dateobject.second)
label = "A2"
outputstring = datestring + "   " + label +"   " + str(savg) + "    " + str(svar)
f = open("arduinolog.txt", 'r')
temp = f.read()
f.close()
f = open("arduinolog.txt", 'w')
f.write(temp + "\n" + outputstring)
f.close()
#print outputstring