import cv2
import numpy as np
from time import sleep

fps = 60                                            # Frames per second of incoming video

incoming_video = cv2.VideoCapture('some_video.mp4')
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
