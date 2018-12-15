#! /usr/bin/env python

import rospy
import rosbag
from audio_common_msgs.msg import AudioData
from std_msgs.msg import UInt32
import os

if __name__ == '__main__':
	os.system("rosbag record -O audio.bag /audio/audio")

	#os.system("rosbag reindex audio.bag --output-dir=/home/sugi/catkin_ws/recorded_video  *.bag")

