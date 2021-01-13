# **VEHICLE RECOGNITION AND COUNTING**
________________________________________________________________________________________________________________________

_This project is a course project for Computer Graphics._

It is a vehicle detection and counting system. This project uses technologies related to computer vision. 
Objects movements and shapes are determined using morphological transformation applied to the image.

System detects vehicle and counts them from incoming video in mp4 (avi) format.

**User guide:**

To run the program you need to install following modules:

- pip install opencv-contrib-python
- pip install numpy

Before running program:

- place the file you want to read video from into project directory

- video must be in a correct format (mp4 / avi)

- you need to rename your video to 'video.mp4' or use one of example videos OR change parameter passed into cv2.VideoCapture()

CAUTION!
Coordinates and dimensions for all UI elements depend on resolution of source video.
By default, all of them are created for HD (1280 * 720) video resolution.

FPS variable must match FPS of income video. 

The effectiveness of the program depends on the quality of the video.

NOT suitable for night traffic.

________________________________________________________________________________________________________________________

## Version 1.0.4
* Added last frame check

## Version 1.0.3
* Added counter for detected vehicle
* Created a line vehicle to cross with  
* Implemented vehicle counting in case of crossing the line
* System calibrating

## Version 1.0.2
* Added minimal threshold for rectangle dimensions to avoid false positives

## Version 1.0.1
* System detects moving objects.
* Visualizing a rectangles around moving objects.
* Example video added.




