# import GPIO library
import RPi.GPIO as GPIO

# set GPIO numbering mode and define input and output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

try:
    while True:
        if GPIO.input(12):
            GPIO.output(11, True)
            GPIO.output(7, False)
        else:
            GPIO.output(11, False)
            GPIO.output(7, True)
        if GPIO.input(16):
            GPIO.output(15, True)
            GPIO.output(13, False)
        else:
            GPIO.output(15, False)
            GPIO.output(13, True)

finally:
    # cleanup the GPIO pins before ending
    GPIO.cleanup()