import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# GPIO.setup(led, GPIO.OUT)
# GPIO.setup(switch, GPIO.IN)

def changePinOut(pin, high):
    if (high):
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)

def cleanUp():
    GPIO.cleanup()
