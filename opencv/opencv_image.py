import cv2

#image 파일 읽기
img = cv2.imread('AKMU.jpg')
img2 = cv2.resize(img, (400, 600))



edge1 = cv2.Canny(img, 50, 100)
edge2 = cv2.Canny(img, 100, 150)
edge3 = cv2.Canny(img, 150, 200)

cv2.imshow('AKMU', img2)
cv2.imshow('edge1', edge1)
cv2.imshow('edge2', edge2)
cv2.imshow('edge3', edge3)
# 키보드 입력을 기다림 (millisecond)
# 기본값 0, 0 인 경우 키보드 입력이 있을 때까지 계속 기다림
cv2.waitKey(0)

# 열려있는 모든 창 닫기
cv2.destroyAllWindows()