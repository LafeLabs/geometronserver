#!/usr/bin/env python
import urllib2
basecube = "https://pastebin.com/raw/L8kF4XXS"
response1 = urllib2.urlopen(basecube)
indexstring = response1.read()
response1.close()
f = open("index.html", 'w')
f.write(indexstring)
f.close()