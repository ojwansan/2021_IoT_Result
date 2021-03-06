import cv2

#image 파일 읽기
img = cv2.imread('AKMU.jpg')
img2 = cv2.resize(img, (400, 600))

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


cv2.imshow('AKMU', img2)
cv2.imshow('AKMU_GRAY', gray)

# 키보드 입력을 기다림 (millisecond)
# 기본값 0, 0 인 경우 키보드 입력이 있을 때까지 계속 기다림
while True:
  if cv2.waitKey() == 13:
    break

cv2.imwrite('AKMU_GRAY.jpg', gray)
# 열려있는 모든 창 닫기
cv2.destroyAllWindows()