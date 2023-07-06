import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def setUp(pin):
    GPIO.setup(pin, GPIO.OUT)

def changePinOut(pin, high):
    if (high):
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)

def cleanUp():
    GPIO.cleanup()
