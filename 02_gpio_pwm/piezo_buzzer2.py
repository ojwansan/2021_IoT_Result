import RPi.GPIO as gpio
import time

buzzerPin = 27
gpio.setmode(gpio.BCM)
gpio.setup(buzzerPin, gpio.OUT)

pwm = gpio.PWM(buzzerPin,262)
pwm.start(10)
#4도~5도
melody = [262, 294, 330, 350, 392, 440, 494, 523]

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)

finally:
    pwm.stop()
    gpio.cleanup()