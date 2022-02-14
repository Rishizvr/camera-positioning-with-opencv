# Camera Positioning System
v1 - 2021-12-05 <br/>
Simulation uses a Python program with OpenCV library for computer vision. This program searches for an image and states which direction the camera should move so that it moves in its direction.
## Demo: https://youtu.be/Kk6x1lHnKw8
## Introduction
OpenCV is an open source computer vision library that is supported on Windows, Mac OS, and Linux operating systems. It can be interfaced with C++ and Python programs. The proposed algorithm for feature extraction is the scale-invariant feature transform (SIFT). It offers the ability to identify objects among clutter and occlusion while performing nearly at real-time (Lowe). 4 points are required for the transformation matrix and so that is the minimum number of matches needed. A higher number of matches greatly reduces the chance for false image detection, but also increases computation cost and time. When enough matches are found, a transformation matrix projects the outline of the given image onto the video capture.
## Note:
This program assumes a square image is being used. To use an image with a different number of points, the "dst" index values in the "navi" function can be modified. The (x,y) values of each corner of the detected polygon are stored in the "dst" variable.
## Credit:
SIFT algorithm (https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf). Tutorial by Pysource on computer vision (https://www.youtube.com/watch?v=I8tHLZDDHr4)
