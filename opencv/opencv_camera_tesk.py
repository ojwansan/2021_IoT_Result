import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Failure')
    exit()

while True:
    ret,frame=cap.read()
    if not ret:
        break
    canny = cv2.Canny(frame, 100, 150)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('vid',frame)
    cv2.imshow('gray', gray)
    cv2.imshow('edge',canny)

    if cv2.waitKey(10)==13:
        break

cap.release()
cv2.destroyAllWindows()