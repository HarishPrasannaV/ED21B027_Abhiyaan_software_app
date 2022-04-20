import cv2 as cv
import math
#creating a video capture object
capture=cv.VideoCapture('vids/bolt_test_pothole.mp4')
while True:
    # storing individual frames from video
    isTrue, frame =capture.read()
    # creating a gray scale image
    gray_image= cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #creating a blurred image to reduce noise
    blurred_img= cv.GaussianBlur(gray_image, (5, 5), 0)
    # creating a threshold image by making pixels with gray value less than 220 black and more than 220 white
    _, thresh_image=cv.threshold(gray_image,220,225,cv.THRESH_BINARY)
    #finding the edges from threshold image
    contours, _= cv.findContours (thresh_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours_area = []
    # filtering contours by area
    for cnt in contours:
        area = cv.contourArea(cnt)
        if 700 < area < 1000000000 :
            contours_area.append(cnt)
    contours_cirles = []
    # filtering contours by circularity
    for con in contours_area:
        perimeter = cv.arcLength(con, True)
        area = cv.contourArea(con)
        circularity = 4*math.pi*(area/(perimeter*perimeter))
        if 0.35< circularity < 0.65:
            contours_cirles.append(con)
    # drawing countours on individual frames of video       
    for cnt in contours_cirles:
            cv.drawContours(frame, [cnt],0,(0, 255, 0),3)
    cv.imshow("res",frame)
    # stopping the program if 'esc' key is pressed
    key=cv.waitKey(7)
    if key ==27:
        break
        
capture.release()
# closes the created windows
cv.destroyAllWindows()
