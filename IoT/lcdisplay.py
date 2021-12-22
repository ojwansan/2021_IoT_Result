from lcd import drivers
import time
import Adafruit_DHT
import datetime
now = datetime.datetime.now()
display = drivers.Lcd()
sensor = Adafruit_DHT.DHT11
PIN = 26
humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
def disp(a, b):
  display.lcd_display_string(a, b)
try:
    print('Writing to Display')
    while True:
      now = datetime.datetime.now()
      humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
      nowtime = now.strftime("%x%X")
      if humidity is not None and temperature is not None:
          display.lcd_display_string(nowtime, 1)
          display.lcd_display_string(f"{temperature:.1f}*C, {humidity:.1f}%", 2)
      else:
          print("read error")
finally:
    print("cleaning up")
    display.lcd_clear()