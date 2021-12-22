import picamera
import time

path = '/home/pi/src5/06_multimedia'
now_str = time.strftime("%Y%m%d_%H%M%S")
camera = picamera.PiCamera()

try:
  camera.resolution = (640, 480)
  camera.start_preview()
  time.sleep(3)
  camera.rotation = 180
  
  while True:
    a = int(input("photo : 1, video : 2, exit : 9 >"))
    if a == 1:
      print("사진 촬영")
      camera.capture('%s/photo_%s.jpg' % (path,now_str)) #사진 촬영
    elif a == 2:
      camera.start_recording('%s/video_%s.h264' % (path,now_str)) #동영상 촬영
      input('recoding...\npress enter to stop')
      camera.stop_recording()
    elif a == 9:
      print("종료합니다")
      break
    else:
      print("incorrect command")
finally:
  camera.stop_preview()
