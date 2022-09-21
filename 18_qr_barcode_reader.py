import cv2
from pyzbar import pyzbar

def read_barcode(frame):
    try:
        barcode = pyzbar.decode(frame)
        for barc in barcode:
            x,y,w,h = barcode
            barcode_data = barc.data.decode('utf-8')
            cv2.rectangle(frame,(x,y),(x+w, y+h), (0,255,0),3)
            font = cv2.Formatter_FMT_DEFAULT
            cv2.putText(frame,barcode_data,(x+6,y-6),font,3.0,(255,255,255),1)
            with open("barcode_result.txt", mode ='w') as file:
                file.write("Recognized Barcode:" + barcode_data)
        return frame
    except Exception:
        return Exception
def main():
    try:
        url = input("Enter Yorr Camera URL if you have Remote Camera - ")
        if url != "":
            camera = cv2.VideoCapture(url)
        else:
            camera = cv2.VideoCapture(0)
        while True:
            ret, frame = camera.read()
            if not ret:
                print('We are not reciving any frame')
                break
            if frame is not None:
                frame = read_barcode(frame)
                cv2.imshow('Barcode/QR code reader', frame)
            if cv2.waitKey(1) == ord("q"):
                break
        camera.release()
        cv2.destroyAllWindows()
    except Exception:
        return Exception
main()