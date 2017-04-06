#!/usr/bin/env python
# -*- coding: utf-8 -*-

# USAGE: You need to specify a filter and "only one" image source
#
# (python) range-detector --filter RGB --image /path/to/image.png
# or
# (python) range-detector --filter HSV --webcam

import cv2


def callback(value):
    pass


def setup_trackbars(range_filter, values=[]):
    cv2.namedWindow("Trackbars", 0)

    for index1, i in enumerate(["MIN", "MAX"]):
        v = 0 if i == "MIN" else 255

        for index2, j in enumerate(range_filter):

            if len(values) > index1 and len(values[index1]) > index2:
                v = values[index1][index2]

            cv2.createTrackbar("%s_%s" % (j, i), "Trackbars", v, 255, callback)


def get_trackbar_values(range_filter):
    values = []

    for i in ["MIN", "MAX"]:
        for j in range_filter:
            v = cv2.getTrackbarPos("%s_%s" % (j, i), "Trackbars")
            values.append(v)

    return values


def selectRange(image, filter="HSV", values=[]):

    range_filter = filter

    if range_filter == 'RGB':
        frame_to_thresh = image.copy()
    else:
        frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    setup_trackbars(range_filter, values)

    while True:

        if range_filter == 'RGB':
            frame_to_thresh = image.copy()
        else:
            frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = get_trackbar_values(range_filter)

        thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))

        preview = cv2.bitwise_and(image, image, mask=thresh)
        cv2.imshow("Preview", preview)

        if cv2.waitKey(1) & 0xFF is ord('q'):
            cv2.destroyWindow("Preview")
            cv2.destroyWindow("Trackbars")
            return (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max)

