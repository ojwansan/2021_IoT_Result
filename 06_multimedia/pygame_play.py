import pygame

pygame.init()

pygame.mixer.music.load("sample.mp3")

while True:
  cmd = input('<play: p, pause: pp, unpause: up, stop: s, quit: q>\n')
  if cmd == 'p':
    pygame.mixer.music.play()
    print("playing music")
  elif cmd == 'pp':
    pygame.mixer.music.pause()
    print("pause")
  elif cmd == 'up':
    pygame.mixer.music.unpause()
    print("restart music")
  elif cmd == 's':
    pygame.mixer.music.stop()
    print("stop")
  elif cmd == 'q':
    print("exit")
    break
  else:
    print('incorrect cmd')
