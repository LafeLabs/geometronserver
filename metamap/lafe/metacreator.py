#!/usr/bin/env python
import urllib2
basecube = "";
response = urllib2.urlopen(basecube)
hypercubestring = response.read()
response.close()

def byteCode2string(inputcode):
    inputarray = inputcode.split(",")
    outputstring = ""
    for index in range(len(inputarray)):
        if len(inputarray[index]) > 0:
            #print chr(int(inputarray[index],8))
            outputstring += chr(int(inputarray[index],8))
    return outputstring