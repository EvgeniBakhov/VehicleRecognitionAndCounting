# **VEHICLE RECOGNITION AND COUNTING**
________________________________________________________________________________________________________________________

_This project is a course project for Computer Graphics._

It is a vehicle detection and counting system. This project uses technologies related to computer vision. 
Objects movements and shapes are determined using morphological transformation applied to the image.

System detects vehicle and counts them from incoming video in mp4 format.

**User guide:**

To run the program you need to install following modules:

pip install opencv-contrib-python
pip install numpy

Before running program:

- place the file you want to read video from into project directory

- video must be in a correct format (mp4)

- you need to rename your video to 'video.mp4' or use one of example videos OR change parameter passed into cv2.VideoCapture()

________________________________________________________________________________________________________________________

##Version 1.0.2
* Added minimal threshold for rectangle dimensions to avoid false positives

##Version 1.0.1
* System detects moving objects.
* Visualizing a rectangles around moving objects.
* Example video added.




