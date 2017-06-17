#!/usr/bin/env python

f = open("byte.txt", 'r')
byte = f.read()
f.close()

f = open("goutput.txt",'r')
derp = f.read()
f.close()

f = open("goutput.txt", 'w')
f.write(derp +  "," + byte)
f.close()