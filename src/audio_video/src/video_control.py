#!/usr/bin/env python

import os, signal
import rospy
from std_msgs.msg import String
import subprocess

vid_rec = None

def terminate_process_and_children(p):
 	import psutil
	process = psutil.Process(p.pid)
	for sub_process in process.children(recursive=True):
		sub_process.send_signal(signal.SIGINT)
	p.wait()  # we wait for children to terminate


def callback(data):
    if data.data == "start":
	global vid_rec
    	vid_rec = subprocess.Popen(["roslaunch", "video_recorder", "recorder.launch"])

    if data.data == "stop":
	os.killpg(os.getpgid(vid_rec.pid), signal.SIGTERM)

def listener():

    rospy.init_node('command_listener', anonymous=True)

    rospy.Subscriber('voice_command', String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()

