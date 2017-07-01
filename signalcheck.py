#!/usr/bin/python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.IN)
x = GPIO.input(2)
f = open("/var/www/html/signal/signallog.txt", 'w')
f.write(str(x))
f.close()