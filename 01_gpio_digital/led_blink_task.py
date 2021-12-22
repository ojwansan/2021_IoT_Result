import RPi.GPIO as GPIO
import time

(a) = input("숫자를 입력하세요 :")
print(a)
i = 1
while (i<100):
    LED_PIN = 4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    

    GPIO.output(LED_PIN, GPIO.HIGH)
    print("RED on")
    time.sleep(0.05)
    GPIO.output(LED_PIN, GPIO.LOW)


    LED_PIN = 14
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)


    GPIO.output(LED_PIN, GPIO.HIGH)
    print("YELLOW on")
    time.sleep(0.05)
    GPIO.output(LED_PIN, GPIO.LOW)


    LED_PIN = 3
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)


    GPIO.output(LED_PIN, GPIO.HIGH)
    print("green on")
    time.sleep(0.05)
    GPIO.output(LED_PIN, GPIO.LOW)

    i += 1
    print(i)   
print("끝!!")
print("총"+str(i)+"번 반복했습니다") 

GPIO.cleanup()