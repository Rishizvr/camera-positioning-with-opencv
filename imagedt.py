#
#
# credit: David G. Lowe, SIFT algorithm (https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf)
# credit: Sergio Canu (Pysource), source code (https://pysource.com/2018/03/21/feature-detection-sift-surf-obr-opencv-3-4-with-python-3-tutorial-25/)

import cv2
import numpy as np
import math
import sys

img = cv2.imread("grandcanyon_jimmkidd-alamy.jpg", cv2.IMREAD_GRAYSCALE)

sift = cv2.xfeatures2d.SIFT_create()
kp_image, desc_image = sift.detectAndCompute(img, None)

index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = cv2.FlannBasedMatcher(index_params, search_params)

cap = cv2.VideoCapture(0)
x  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 640 webcam
y  = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 480 webcam
midx = int(x/2)
midy = int(y/2)

def getQuadrant(frame, startPt, endPt, clr, thickness):
	return cv2.rectangle(frame, startPt, endPt, clr, thickness)

def showQuadrants(frame):
	global x, y

	quad1 = getQuadrant(frame, (0, 0), (int(x/2), int(y/2)), (255, 0, 0), 2)
	quad2 = getQuadrant(frame, (int(x/2), 0), (int(x), int(y/2)), (0, 255, 0), 2)
	quad3 = getQuadrant(frame, (0, int(y/2)), (int(x/2), int(y)), (0, 0, 255), 2)
	quad4 = getQuadrant(frame, (int(x/2), int(y/2)), (int(x), int(y)), (255, 255, 0), 2)

def navi(dst):
	global x, y

	if len(dst) == 4:
		print("\n\n===========")

		topLeftPointX = dst[0][0][0]
		topLeftPointY = dst[0][0][1]
		bottomRightPointX = dst[2][0][0]
		bottomRightPointY = dst[2][0][1]

		if ((topLeftPointX < midx) & (topLeftPointY < midy) & ((bottomRightPointY > midy) & (bottomRightPointX > midx))):
			print("move forward")
		else:
			if (topLeftPointX < midx and bottomRightPointX < midx):
				print("move left")
			if (topLeftPointX > midx and bottomRightPointX > midx):
				print("move right")
			if (topLeftPointY < midy and bottomRightPointY < midy):
				print("move up")
			if (topLeftPointY > midy and bottomRightPointY > midy):
				print("move down")



def getHomography(frame, frameGray):
	kp_grayframe, desc_grayframe = sift.detectAndCompute(frameGray, None)

	if len(kp_grayframe) > 3:
		matches = flann.knnMatch(desc_image, desc_grayframe, k=2)

		good_points = []
		for m, n in matches:
			if m.distance < 0.5*n.distance: 
				good_points.append(m)

		if len(good_points) > 7:
			query_pts = np.float32([kp_image[m.queryIdx].pt for m in good_points]).reshape(-1, 1, 2)
			train_pts = np.float32([kp_grayframe[m.trainIdx].pt for m in good_points]).reshape(-1, 1, 2)

			matrix, mask = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)
			matches_mask = mask.ravel().tolist()

			if matrix is not None:
				h, w = img.shape
				pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
				dst = cv2.perspectiveTransform(pts, matrix)
				homography = cv2.polylines(frame, [np.int32(dst)], True, (255, 0, 0), 3)

				showQuadrants(homography)
				navi(dst)
				cv2.imshow("Homography", homography)
			else:
				showQuadrants(frame)
				cv2.imshow("Homography", frame)
		else:
			showQuadrants(frame)
			cv2.imshow("Homography", frame)
	else:
		showQuadrants(frame)
		cv2.imshow("Homography", frame)

while(True):
	success, frame = cap.read();

	frameBlur = cv2.GaussianBlur(frame, (7, 7), 1)
	frameGray = cv2.cvtColor(frameBlur, cv2.COLOR_BGR2GRAY)

	getHomography(frame, frameGray)
	
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

cap.release()
cv2.destroyAllWindows()