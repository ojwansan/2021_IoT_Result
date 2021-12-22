import RPi.GPIO as GPIO
import time

LED_PIN = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        val = input("0 : 0ff, 1 : on, 2 : blink, 3 : sos, 9 : exit ")
        if val == '0':
            GPIO.output(LED_PIN, GPIO.LOW)
            print("led off")
        elif val == '1':
            GPIO.output(LED_PIN, GPIO.HIGH)
            print("led on")
        elif val == '2':
            n = int(input())
            for i in range(n):
                GPIO.output(LED_PIN, GPIO.HIGH)
                print("led on")
                time.sleep(1)
                GPIO.output(LED_PIN, GPIO.LOW)
                print("led off")
                time.sleep(1)
        elif val == '3':
            while True:
                for i in range(3):
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    time.sleep(0.07)
                    GPIO.output(LED_PIN, GPIO.LOW)
                    time.sleep(0.07)
                time.sleep(0.1)
                for i in range(3):
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(LED_PIN, GPIO.LOW)
                    time.sleep(0.5)
                time.sleep(0.1)
                for i in range(3):
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    time.sleep(0.07)
                    GPIO.output(LED_PIN, GPIO.LOW) 
                    time.sleep(0.07)
                time.sleep(1)
        elif val == '9':
            break
        else :
            print("????????????????????????????????")
finally:
    GPIO.cleanup()


print("cleanup and exit")   
    