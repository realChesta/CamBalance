import cv2
import imutils
import numpy as np
from collections import deque

from rangeDetector import selectRange


def track(onNewCoordinate):
    # start webcam
    camera = cv2.VideoCapture(1)

    lowerColor = (169, 140, 131)
    upperColor = (180, 255, 255)
    pointHistory = deque(maxlen=30)

    while True:
        # get current webcam frame
        (grabbed, frame) = camera.read()

        # resize and convert frame to hsv
        frame = imutils.resize(frame, width=600)
        copy = frame.copy()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # generate mask
        mask = cv2.inRange(hsv, lowerColor, upperColor)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # find contours of the ball ([-2] for compatibility)
        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        if len(contours) > 0:
            # find largest contour
            c = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            onNewCoordinate(center)

            # TODO: find minimum radius
            if radius > 5:
                # draw outline and center of tracked ball
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)

        pointHistory.appendleft(center)

        # draw history
        for i in range(1, len(pointHistory)):
            if pointHistory[i - 1] is None or pointHistory[i] is None:
                continue

            thickness = int(np.sqrt(pointHistory.maxlen / float(i + 1)) * 2.5)
            cv2.line(frame, pointHistory[i - 1], pointHistory[i], (0, 0, 255), thickness)

        cv2.imshow("Frame", frame)

        # exit on 'q'
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('a'):
            (lowerColor, upperColor) = selectRange(copy, values=(lowerColor, upperColor))
            print("lowerColor: " + str(lowerColor))
            print("upperColor: " + str(upperColor))

    camera.release()
    cv2.destroyAllWindows()
