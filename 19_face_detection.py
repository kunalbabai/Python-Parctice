import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('.xml')
url = input("Enter Yorr Camera URL if you have Remote Camera - ")
if url != "":
    camera = cv2.VideoCapture(url)
else:
    camera = cv2.VideoCapture(0)
# To capture video from webcam. 
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = camera.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
camera.release()



####form image 
# import cv2
# face = cv2.CascadeClassifier(r"C:\Users\UDCIND\OneDrive - UDC\Smaple_Program_ML\.xml")
# img = cv2.imread(r"C:\Users\UDCIND\OneDrive - UDC\Smaple_Program_ML\istockphoto-1368965646-170667a.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = face.detectMultiScale(gray,1.1,4)
# for (x, y, w, h) in faces: 
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# cv2.imshow('img',img)
# cv2.waitKey()
# # cv2.imwrite("face_detected.png", img) 
# # print('Successfully saved')