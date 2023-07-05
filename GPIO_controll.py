import RPi.GPIO as GPIO
import time

def changePinOut(pin, high):
    if (high):
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)

GPIO.cleanup()