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
import imageio

reader1 = imageio.get_reader('videos/moto.mp4')
reader2 = imageio.get_reader('videos/note.mp4')
fps1 = reader1.get_meta_data()['fps']
fps2 = reader2.get_meta_data()['fps']

writer = imageio.get_writer('output.mp4', fps = fps)

while i in enumerate(reader):
	left = fps1.read()
	right = fps2.read()

	# resize the frames
	left = imutils.resize(left, width=400)
	right = imutils.resize(right, width=400)

	# stitch the frames together to form the panorama
	# IMPORTANT: you might have to change this line of code
	# depending on how your cameras are oriented; frames
	# should be supplied in left-to-right order
	result = stitcher.stitch([left, right])

	# stitch the frames together to form the panorama
	# IMPORTANT: you might have to change this line of code
	# depending on how your cameras are oriented; frames
	# should be supplied in left-to-right order
	result = stitcher.stitch([left, right])
	gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)
	# locs = motion.update(gray)


	# no homograpy could be computed
	if result is None:
		print("[INFO] homography could not be computed")
		break

	# convert the panorama to grayscale, blur it slightly, update
	# the motion detector
	gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)
	locs = motion.update(gray)
	cv2.imshow("Result", result)
	cv2.imshow("Left Frame", left)
	cv2.imshow("Right Frame", right)


# for i, frame in enumerate(reader):
#     frame = detect(frame, net.eval(), transform)
#     writer.append_data(frame)
#     print(i)
# writer.close()

# # initialize the video streams and allow them to warmup
# print("[INFO] starting cameras...")
# rightStream = VideoStream(src="https://10.122.180.236:8080/video").start()
# leftStream = VideoStream(src="http://192.168.43.162:8080/video").start()
# time.sleep(2.0)

# # initialize the image stitcher, motion detector, and total
# # number of frames read
# stitcher = Stitcher()
# motion = BasicMotionDetector(minArea=500)
# total = 0

# loop over frames from the video streams
# while True:
	# grab the frames from their respective video streams
	# left = leftStream.read()
	# right = rightStream.read()

	# # resize the frames
	# left = imutils.resize(left, width=400)
	# right = imutils.resize(right, width=400)

	# # stitch the frames together to form the panorama
	# # IMPORTANT: you might have to change this line of code
	# # depending on how your cameras are oriented; frames
	# # should be supplied in left-to-right order
	# result = stitcher.stitch([left, right])
	# gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
	# gray = cv2.GaussianBlur(gray, (21, 21), 0)
	# locs = motion.update(gray)


	# # no homograpy could be computed
	# if result is None:
	# 	print("[INFO] homography could not be computed")
	# 	break

	# # convert the panorama to grayscale, blur it slightly, update
	# # the motion detector
	# gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
	# gray = cv2.GaussianBlur(gray, (21, 21), 0)
	# locs = motion.update(gray)
	# cv2.imshow("Result", result)
	# cv2.imshow("Left Frame", left)
	# cv2.imshow("Right Frame", right)

# 	key = cv2.waitKey(1) & 0xFF
# 	# only process the panorama for motion if a nice average has
# 	# been built up
# 	if total > 32 and len(locs) > 0:
# 		# initialize the minimum and maximum (x, y)-coordinates,
# 		# respectively
# 		(minX, minY) = (np.inf, np.inf)
# 		(maxX, maxY) = (-np.inf, -np.inf)

# 		# loop over the locations of motion and accumulate the
# 		# minimum and maximum locations of the bounding boxes
# 		for l in locs:
# 			(x, y, w, h) = cv2.boundingRect(l)
# 			(minX, maxX) = (min(minX, x), max(maxX, x + w))
# 			(minY, maxY) = (min(minY, y), max(maxY, y + h))

# 		# draw the bounding box
# 		cv2.rectangle(result, (minX, minY), (maxX, maxY),
# 			(0, 0, 255), 3)

# 	# increment the total number of frames read and draw the 
# 	# timestamp on the image
# 	total += 1
# 	timestamp = datetime.datetime.now()
# 	ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
# 	cv2.putText(result, ts, (10, result.shape[1] - 10),
# 	cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

# 	# show the output images
# 	cv2.imshow("Result", result)
# 	cv2.imshow("Left Frame", left)
# 	cv2.imshow("Right Frame", right)
# 	key = cv2.waitKey(1) & 0xFF

# 	# if the `q` key was pressed, break from the loop
# 	if key == ord("q"):
# 		break

# # do a bit of cleanup
# print("[INFO] cleaning up...")
# cv2.destroyAllWindows()
# leftStream.stop()
# rightStream.stop()