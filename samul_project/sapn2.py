#import 받기
from flask import Flask, render_template, request
import time as t
import RPi.GPIO as G
from lcd import drivers
import datetime


app = Flask(__name__)

display = drivers.Lcd()

BUP = 5
BTP = 11
BP = 26
GP = 19
YP = 13
RP = 6
#GPIO 설정
G.setmode(G.BCM)
G.setup(BUP, G.OUT)
G.setup(BTP, G.OUT)
pwm = G.PWM(BUP, 262)
G.setup(RP, G.OUT)
G.setup(GP, G.OUT)
G.setup(BP, G.OUT)
G.setup(YP, G.OUT)
G.output(RP, G.LOW)
G.output(GP, G.LOW)
G.output(BP, G.LOW)
G.output(YP, G.LOW)

#홈 라우팅
@app.route("/")
def home():
  return render_template("sa.html")

@app.route("/timer", methods={'GET', 'POST'})
def timef():
  #html에서 데이터 받기
  if(request.method == 'POST'):
    hour = float(request.form['inptime'])
    min = float(request.form['inpmin'])
    sec = float(request.form['inpsec'])
    time = hour*3600+min*60+sec
  #시간에 따라 LED 색 변경
  while time != 0:
    if(time > 3600):
      G.output(BP, G.HIGH)
    elif(time<=3600 and time>600):
      G.output(BP, G.LOW)
      G.output(GP, G.HIGH)
    elif(time<=600 and time > 10):
      G.output(GP, G.LOW)
      G.output(YP, G.HIGH)
    elif(time<=10):
      G.output(YP, G.LOW)
      G.output(RP, G.HIGH)
    #LCD에 남은 시간 표시
    display.lcd_display_string("Until the alarm goes off...", 1)
    display.lcd_display_string(str(datetime.timedelta(seconds=time)), 2)
    t.sleep(1)
    time = time-1
  #알람
  while G.input(BTP) != 1:
    display.lcd_display_string("The time is up!", 1)
    display.lcd_display_string("00:00:00", 2)
    G.output(RP, G.HIGH)
    pwm.start(10)
    t.sleep(0.5)
    display.lcd_clear()
    G.output(RP, G.LOW)
    pwm.stop()
    t.sleep(0.5)
  G.cleanup()
  display.lcd_clear()
  return '''<a href = "/"><font size="5">돌아가기</a>'''


if __name__ == "__main__":
  try:
    app.run(host="0.0.0.0")
  finally:
    G.cleanup()
    display.lcd_clear()