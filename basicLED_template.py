#!/usr/bin/python
'''Turn an LED on and off
   basicLED.py --Frank M.'''
   
import RPi.GPIO as GPIO
import time

pinLED = 16
timeDelay = .5  # in seconds

def main():

    print "Starting Script..."

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinLED,GPIO.OUT)  #  declare pinLED as an output

    #Add code here...

    GPIO.cleanup()
    print "..................Completed"

if __name__=="__main__":
    main()
