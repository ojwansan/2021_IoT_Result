import RPi.GPIO as gpio
import time

ledPin = 4
gpio.setmode(gpio.BCM)
gpio.setup(ledPin, gpio.OUT)

gpio.PWM(ledPin, 50)
pwm.start(0)

try:
    for i in range(3):
        for j in range(0, 101, 5):
            pwm.ChangeDutyCycle(j)
            time.sleep(0.1)
        for j in range(100, -1, -5):
            pwm.ChangeDutyCycle(j)
            time.sleep(0.1)
finally:
    pwm.stop()
    gpio.cleanup()