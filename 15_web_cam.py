import cv2 as cv
#url = 'https://192.168.1.6:8080/video'
url = 'https://100.64.201.42:8080/video'
cap = cv.VideoCapture(url)
if not cap.isOpened():
    print("Cannot Open Camera!!!!")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print('We are not reciving any frame')
        break
    if frame is not None:
        cv.imshow('Frame',frame)
    q = cv.waitKey(1)
    if q == ord("q"):
        break
cap.release()
cv.destroyAllWindows()