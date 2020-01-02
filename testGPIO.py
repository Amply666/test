#!/usr/bin/python
# coding=utf-8
import time
import RPi.GPIO as GPIO
# Power is 5V(pin 2) and GND is pin6 pin_list = [3, 5, 7, 11, 13, 15, 19, 21] p$
#[11, 13]
pin_list = [3,5,7,11,13,15,19,21]
GPIO.setmode(GPIO.BOARD)
for pin in pin_list:
    GPIO.setup(pin, GPIO.OUT)

def trigger_pins(mode=GPIO.LOW, delay=0):
    for pin in pin_list:
        print 'pin: ' + str(pin) + ' mode: ' + str(mode)
        GPIO.output(pin, mode)
        time.sleep(delay)

trigger_pins(mode=GPIO.HIGH, delay=1)
