import cv2
import imutils

from rangeDetector import selectRange

lowerColor = (169, 140, 131)
upperColor = (180, 255, 255)

# start webcam
camera = cv2.VideoCapture(1)

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

        # TODO: find minimum radius
        if radius > 5:
            # draw outline and center of tracked ball
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

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
