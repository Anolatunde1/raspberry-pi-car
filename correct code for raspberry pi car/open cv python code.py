import cv2
import cvzone
cap = cv2.VideoCapture(0)
my_classfier = Classifier('C:\Users\USER\Desktop\raspberry pi car\correct code for raspberry pi car\model\keras_model.h5', '"C:\Users\USER\Desktop\raspberry pi car\correct code for raspberry pi car\model\labels.txt"')

while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)
