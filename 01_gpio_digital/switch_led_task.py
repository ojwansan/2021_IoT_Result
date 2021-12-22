import RPi.GPIO as gpio

RED_PIN = 5
YELLOW_PIN = 6
BLUE_PIN = 22
GREEN_PIN = 8
buzzerPin = 27
gpio.setmode(gpio.BCM)
#4도~5도
melody = [262, 294, 330, 350, 392, 440, 494, 523]

gpio.setup(buzzerPin, gpio.OUT)
gpio.setup(RED_PIN, gpio.OUT)
gpio.setup(YELLOW_PIN, gpio.OUT)
gpio.setup(GREEN_PIN, gpio.OUT)
gpio.setup(BLUE_PIN, gpio.OUT)
#pwm.ChangeFrequency(i)
pwm = gpio.PWM(buzzerPin,262)
pwm.start(10)
val = 1
try:
    while True:
        gpio.output(RED_PIN, val)
        gpio.output(YELLOW_PIN, val)
        gpio.output(BLUE_PIN, val)
        gpio.output(GREEN_PIN, val)
finally:
    gpio.cleanup()
    print('cleanup and exit')
