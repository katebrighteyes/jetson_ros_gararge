#!/usr/bin/env python3

import cv2, rospy, time
import numpy as np
import pyrealsense2
from realsense_depth import *

print(1)
rospy.init_node('test_depth_node')
print(2)
point = (400, 300)
print(3)
dc = DepthCamera()
print(4)
cv2.namedWindow("Color frame")


while not rospy.is_shutdown():
	ret, depth_frame, color_frame = dc.get_frame()

	if not ret:
		continue

	vallist = []
	totval = 0
	distance = depth_frame[320, 240]
	#print('distance:{}'.format(distance))
	point = (320, 240)
	cv2.circle(color_frame, point, 4, (0, 0, 255))

	if distance > 0 and distance < 200:
		print('center distance in 20 cm:{}'.format(distance))

		cv2.putText(color_frame, "distance in 20 cm:{}".format(distance/10), (30, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

	cv2.imshow("depth frame", depth_frame)
	cv2.imshow("Color frame", color_frame)
	key = cv2.waitKey(1)
	if key == 27:
		break

cv2.destroyAllWindows()

