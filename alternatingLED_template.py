#!/usr/bin/python
'''Alternate between two LEDs
   alternatingLED.py --Frank M.'''
   
import RPi.GPIO as GPIO
import time

pinLED1 = 16
pinLED2 = 18
timeDelay = .3  # in seconds

def main():

    print "Starting Script..."

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinLED1, GPIO.OUT)  #  declare pinLED1 as an output
    GPIO.setup(pinLED2, GPIO.OUT)  #  declare pinLED2 as an output
    
    #Add code here...
        
    GPIO.cleanup()
    print "..................Completed"

if __name__=="__main__":
    main()
