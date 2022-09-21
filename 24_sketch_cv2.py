#creating a function to Convert RGB Image to GrayScale Image  like Sketch Image (Frawing)
# def color_sketch(img):
#     try:
#         import cv2
#         #opening the image using cv2

#         image = cv2.imread(img)
#         cv2.imshow("Dog", image)
#         cv2.waitKey(0)

#         #converting garyscale image 
#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         cv2.imshow("Dog_New", gray)
#         cv2.waitKey(0)

#         inverted_image = 255 - gray
#         cv2.imshow("Inverted", inverted_image)
#         cv2.waitKey(0)

#         blured = cv2.GaussianBlur(inverted_image,(5,5),cv2.BORDER_DEFAULT)
#         cv2.imshow("Blured", blured)
#         cv2.waitKey(0)
#         #inverted blurred 
#         inv_blurred = 255 - blured
#         cv2.imshow("Inv Blured", inv_blurred)
#         cv2.waitKey(0)

#         pencil_sketch = cv2.divide(gray, inv_blurred, scale=256.0)
#         cv2.imshow("Sketch", pencil_sketch)
#         cv2.waitKey(0)
#     except Exception:
#         return Exception

# color_sketch(r"C:\Users\UDCIND\OneDrive - UDC\Smaple_Program_ML\istockphoto-1368965646-170667a.jpg")


import cv2
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
    # convert to invert
    invert_gray = 255 - gray
    #converting the inverted image to blur image
    blur = blured = cv2.GaussianBlur(invert_gray,(5,5),cv2.BORDER_DEFAULT)
    #converting the blur inverted image to invert
    blur_inv = 255 - blur
    pencil_sketch = cv2.divide(gray, blur_inv, scale=256.0)
    # Display
    cv2.imshow('img', pencil_sketch)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
camera.release()