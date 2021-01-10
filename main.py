# ©Created by Yevhen Bakhov, 2021.

import cv2
import numpy as np
from time import sleep

fps = 60                                            # Frames per second of incoming video

min_rect_width = 50
min_rect_height = 50

incoming_video = cv2.VideoCapture('video.mp4')
subtractor = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    self, original_video = incoming_video.read()    # Reading from input video stream
    time = float(1 / fps)
    sleep(time)                                     # Waiting for the next frame

    # Turns original colors into grayscale
    grayscale = cv2.cvtColor(original_video, cv2.COLOR_BGR2GRAY)

    # Blur for smoothing boundaries
    blurred = cv2.GaussianBlur(grayscale, (3, 3), 5)

    # Separates background and creates foreground mask for easier detection
    subtracted = subtractor.apply(blurred)

    # Provides image dilation
    dilated = cv2.dilate(subtracted, np.ones((5, 5)))

    # Get kernel with ellipse form and size 5x5
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

    # Creates video with dilated contours of the vehicles
    dilated_contours_video = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
    dilated_contours_video = cv2.morphologyEx(dilated_contours_video, cv2.MORPH_CLOSE, kernel)

    # Finds contours
    contours, hierarchy = cv2.findContours(dilated_contours_video, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for(i, c) in enumerate(contours):
        (x, y, width, height) = cv2.boundingRect(c)     # Creates a rectangle around the contours

        valid_dimensions = (width >= min_rect_width) and (height >= min_rect_height)
        if not valid_dimensions:        # If rectangle smaller then minimal dimensions values
            continue                    # we do not detect the vehicle

        cv2.rectangle(original_video, (x, y), ((x + width), (y + height)), (0, 0, 255), 1)    # Visualize a rectangle

    # Shows a window with video with contours of the vehicles
    cv2.imshow("Contours", dilated_contours_video)

    # Shows an original video
    cv2.imshow("Original video stream", original_video)

    if cv2.waitKey(1) == 27:        # Key to exit program (ESC)
        break

cv2.destroyAllWindows()
incoming_video.release()
