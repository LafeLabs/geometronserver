#!/usr/bin/env python
import serial
ser = serial.Serial('/dev/cu.usbmodemFD111')  # open serial port
ser.baudrate = 115200
stringout = ""
for count in range(100):
    rawdata = ser.readlines(3100)
    for index in range(len(rawdata)):
        rawdata[index] = rawdata[index].strip()
        stringout += rawdata[index] + ","
    stringout += "\n"
print stringout