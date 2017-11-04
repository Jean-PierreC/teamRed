import cv2
import numpy as np
        count = -1

Video_capture = cv2.VideoCapture(0)

        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        THRESHOLD_MIN = np.array([70, 0, 0],np.uint8)
        THRESHOLD_MAX = np.array([110, 255,255],np.uint8)

        frame = cv2.inRange(img_hsv, THRESHOLD_MIN,THRESHOLD_MAX)
        image, contours, count, = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


        for cont in contours:
            count = count +1
            approx = cv2.approxPolyDp(cont, epsilon, True)

            if cv2.contourArea(approx) > 5000 and len(approx) == 4:
                cv2.drawContours(image, contours, count,(255,255,255), 10)
                imshow("sls",image)

