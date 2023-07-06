import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def setUp(pinArray):
    for pin in pinArray:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

def changePinOut(pin, high):
    if (high):
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)

def cleanUp():
    GPIO.cleanup()
