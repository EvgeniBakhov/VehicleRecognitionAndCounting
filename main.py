# ©Created by Yevhen Bakhov, 2021.

import cv2
import numpy as np
from time import sleep

# Frames per second of incoming video
fps = 60

min_rect_width = 50
min_rect_height = 50

counting_line_pos = 560

# Permissible error between the line and center
error_offset = 7

# Array which contains all detected vehicles
detected = []

# Counter for detected vehicles
vehicle_counter = 0

incoming_video = cv2.VideoCapture('videos/test_video.mp4')
subtractor = cv2.bgsegm.createBackgroundSubtractorMOG()


def find_center(x_pos, y_pos, rect_width, rect_height):     # We use center of the rectangle with vehicle inside to
    x_offset = int(rect_width / 2)                          # count vehicles easier (collides with line)
    y_offset = int(rect_height / 2)
    center_x = x_pos + x_offset
    center_y = y_pos + y_offset
    return center_x, center_y


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

    # Displays a line for counting vehicles
    cv2.line(original_video, (30, counting_line_pos), (1200, counting_line_pos), (255, 0, 0), 3)

    for(i, c) in enumerate(contours):
        (x, y, width, height) = cv2.boundingRect(c)     # Creates a rectangle around the contours

        valid_dimensions = (width >= min_rect_width) and (height >= min_rect_height)
        if not valid_dimensions:        # If rectangle smaller then minimal dimensions values
            continue                    # we do not detect the vehicle

        cv2.rectangle(original_video, (x, y), ((x + width), (y + height)), (0, 0, 255), 1)    # Visualize a rectangle

        center = find_center(x, y, width, height)
        # Add a center of vehicle rectangle to arrays with detected vehicles
        detected.append(center)
        cv2.circle(original_video, center, 4, (0, 0, 255), 3)

        for(x, y) in detected:
            if counting_line_pos + error_offset > y > counting_line_pos - error_offset:     # Collision with the line
                vehicle_counter += 1
                cv2.line(original_video, (30, counting_line_pos), (1200, counting_line_pos), (0, 255, 255), 3)
                cv2.circle(original_video, center, 4, (0, 255, 0), 3)
                cv2.rectangle(original_video, (480, 20), (560, 60), (0, 0, 255), -1)

                # Removing object from the array
                detected.remove((x, y))
                print("Vehicle detected : " + str(vehicle_counter))

    # Displays number of detected vehicles
    cv2.putText(original_video, "Брой превозни средства : " + str(vehicle_counter), (10, 50),
                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2, 5)

    # Shows a window with video with contours of the vehicles
    cv2.imshow("Contours", dilated_contours_video)

    # Shows an original video
    cv2.imshow("Original video stream", original_video)

    # Key to exit program (ESC)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
incoming_video.release()
