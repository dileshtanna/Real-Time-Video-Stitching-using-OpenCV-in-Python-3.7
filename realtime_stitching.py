# USAGE
# python realtime_stitching.py

# import the necessary packages
from __future__ import print_function
from pyimagesearch.basicmotiondetector import BasicMotionDetector
from pyimagesearch.panorama import Stitcher
from imutils.video import VideoStream
import numpy as np
import datetime
import imutils
import time
import cv2

# initialize the video streams and allow them to warmup
print("[INFO] starting cameras...")
# rightStream = VideoStream(src="http://localhost/moto.mp4").start()  #aaka
# leftStream = VideoStream(src="http://localhost/note.mp4").start()  #no aaka
rightStream = VideoStream(src="https://10.18.83.177:8080/video").start()  #aaka
leftStream = VideoStream(src="http://192.168.43.131:8080/video").start()  #no aaka
time.sleep(2.0)

# initialize the image stitcher, motion detector, and total
# number of frames read
stitcher = Stitcher()
motion = BasicMotionDetector(minArea=15000)
total = 0

# loop over frames from the video streams
while True:
	# grab the frames from their respective video streams
	left = leftStream.read()
	right = rightStream.read()

	# resize the frames
	left = imutils.resize(left, width=400)
	right = imutils.resize(right, width=400)

	# stitch the frames together to form the panorama
	# IMPORTANT: you might have to change this line of code
	# depending on how your cameras are oriented; frames
	# should be supplied in left-to-right order
	result = stitcher.stitch([left, right])

	# no homograpy could be computed
	if result is None:
		print("[INFO] homography could not be computed")
		break

	# convert the panorama to grayscale, blur it slightly, update
	# the motion detector
	gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)
	locs = motion.update(gray)

	# only process the panorama for motion if a nice average has
	# been built up
	if total > 32 and len(locs) > 0:
		# initialize the minimum and maximum (x, y)-coordinates,
		# respectively
		(minX, minY) = (np.inf, np.inf)
		(maxX, maxY) = (-np.inf, -np.inf)

		# loop over the locations of motion and accumulate the
		# minimum and maximum locations of the bounding boxes
		# for l in locs:
		# 	(x, y, w, h) = cv2.boundingRect(l)
		# 	(minX, maxX) = (min(minX, x), max(maxX, x + w))
		# 	(minY, maxY) = (min(minY, y), max(maxY, y + h))

		# # draw the bounding box
		# cv2.rectangle(result, (minX, minY), (maxX, maxY),
		# 	(0, 0, 255), 3)

	# increment the total number of frames read and draw the 
	# timestamp on the image
	# total += 1
	# timestamp = datetime.datetime.now()
	# ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
	# cv2.putText(result, ts, (10, result.shape[1] - 10),
	# cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

	# show the output images
	cv2.imshow("Result", result)
	cv2.imshow("Left Frame", left)
	cv2.imshow("Right Frame", right)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
leftStream.stop()
rightStream.stop()