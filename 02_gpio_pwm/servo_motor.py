import RPi.GPIO as gpio
import time

SERVO_PIN = 4
gpio.setmode(gpio.BCM)
gpio.setup(SERVO_PIN, gpio.OUT)

pwm = gpio.PWM(SERVO_PIN, 50)
pwm.start(7.5)  # 0도 설정

try:
    while True:
        val = input('1 : -90, 2: 0, 3 : +90, 9: exit > ')
        if val == '1':
            pwm.ChangeDutyCycle(5) 
        elif val == '2':
            pwm.ChangeDutyCycle(7.5) 
        elif val == '3':
            pwm.ChangeDutyCycle(10) 
        elif val == '9':
            break

finally:
    pwm.stop()
    gpio.cleanup()