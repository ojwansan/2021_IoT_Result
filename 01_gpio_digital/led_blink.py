import RPi.GPIO as GPIO
import time


RED = 5
YELLOW = 6
BLUE = 7
GREEN = 8
PIN = [RED, YELLOW, BLUE, GREEN]
GPIO.output(RED, GPIO.LOW)
GPIO.output(YELLOW, GPIO.LOW)
GPIO.output(BLUE, GPIO.LOW)
GPIO.output(GREEN, GPIO.LOW)    
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

try :
    while True:
        for i in PIN:
            GPIO.output(PIN, GPIO.HIGH)
            print(PIN + "on")
            time.sleep(1)
            GPIO.output(PIN, GPIO.LOW)
            print(PIN + "off")
            time.sleep(1)

finally:
    #코드 종료 후 GPIO 초기화
    print("\nend of porgram")
    GPIO.output(RED, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(BLUE, GPIO.LOW)
    GPIO.output(GREEN, GPIO.LOW)    
    GPIO.cleanup()