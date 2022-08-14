# Local Positioning System
v1 - 2021-12-05 <br/>
## Credit:
SIFT algorithm (https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf). <br/>
Tutorial by Pysource on computer vision (https://www.youtube.com/watch?v=I8tHLZDDHr4) <br/>
## Demo: https://youtu.be/Kk6x1lHnKw8
## Introduction
This UAV guidance simulation uses a Python program and the OpenCV computer vision library. The computer searches for an image and calculates which direction to move so that it moves towards it. OpenCV is an open source computer vision library that is supported on Windows, Mac OS, and Linux operating systems. It can be interfaced with C++ and Python programs. The proposed algorithm for feature extraction is the scale-invariant feature transform (SIFT). It offers the ability to identify objects among clutter and occlusion while performing nearly at real-time (Lowe). 4 points are required for the transformation matrix and so that is the minimum number of matches needed. A higher number of matches greatly reduces the chance for false image detection, but also increases computation cost and time. When enough matches are found, the outline of the given image is projected onto the video.
