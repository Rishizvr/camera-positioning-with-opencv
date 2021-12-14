# Camera Positioning System
v1 - 2021-12-05 <br/>
Camera guidance system for drone using Python program and OpenCV library. This project uses SIFT algorithm for feature extraction, FLANN-based feature matching, and homography transformation matrix for detecting an uploaded image in a video.
## Demo: https://youtu.be/Kk6x1lHnKw8
## Introduction
OpenCV is an open source computer vision library that is supported on Windows, Mac 
OS, and Linux operating systems. It can be interfaced with C++ and Python programs. By using 
image processing methods from the OpenCV library and applying them to grayscale images, a 
vision positioning system is efficiently prototyped in Python. 
The suggested algorithm for feature extraction is the scale-invariant feature transform 
(SIFT). SIFT is a method for feature extraction developed by David G. Lowe in 2004. It offers 
the ability to identify objects among clutter and occlusion while performing nearly at real-time 
(Lowe 1). Lowe’s algorithm uses a series of steps and only applies the more expensive 
operations at locations that pass an initial test. It extracts distinct features from images and 
reliably matches them with different views of an object or scene. The feature vectors are meant 
to be invariant to scaling, rotation, and translation. At least 3 features should be 
correctly matched from each object for reliable identification. 4 points are required for the 
homography transformation matrix and so that is the minimum number of matches needed. A 
higher number of matches greatly reduces the chance of false detections. Keypoint descriptors 
are highly distinctive. A single feature can find its correct match with good probability in a large 
database of features. In a cluttered image, there is a higher chance of false matches. Next, 
features are matched between the uploaded image and from each frame of the camera stream. A 
nearest-neighbor approximation is used to reduce calculation times. Finally, when enough matches 
are found, a homography transformation matrix projects the outline of the given image onto the 
video capture by determining how far apart the key points are in the original image versus the distances 
between the similar key points in the video stream.
## How to Use:
This program assumes a square image is being used. For use with a geometric shape with a different number of points, change the "dst" index values which are found in the "navi" function. The (x,y) values of each corner of the detected polygon are stored in the "dst" variable and are assigned counter-clockwise. One can replace print statements with movement commands, and the image import can be changed to a different image for tracking. An image is followed by segmenting the video frames into four regions, but this can be modified in the "navi" function to use a different number of regions or to specify different regions of the camera's view.
## Credit:
See David G. Lowe's research on scale-invariant feature transform (SIFT) algorithm (https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf). See tutorial by Pysource on homography in computer vision (https://www.youtube.com/watch?v=I8tHLZDDHr4)
