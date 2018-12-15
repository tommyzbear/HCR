#!/usr/bin/env python

import os, signal
import rospy
from std_msgs.msg import String
import subprocess

audio_cap = None
bag2wav = None
audio_bag = None


def terminate_process_and_children(p):
 	import psutil
	process = psutil.Process(p.pid)
	for sub_process in process.children(recursive=True):
		sub_process.send_signal(signal.SIGINT)
	p.wait()  # we wait for children to terminate

def talker():
	pub = rospy.Publisher('video_audio_ready', String, queue_size=10)
        #rospy.init_node('talker', anonymous=True)
        ready_str = "ready"
        rospy.loginfo(ready_str)
        pub.publish(ready_str)

def callback(data):
    if data.data == "start":
	global audio_cap
	global audio_bag
	global bag2wav
	audio_cap = subprocess.Popen(["roslaunch", "audio_capture", "capture.launch"])
	audio_bag = subprocess.Popen(["rosrun", "audio_video", "audio_bag.py"])


    if data.data == "stop":
	terminate_process_and_children(audio_bag)

	os.killpg(os.getpgid(audio_cap.pid), signal.SIGTERM)

	audio_convert = subprocess.Popen(["rosrun", "audio_convert", "bag2wav"])

	os.system("rosrun audio_convert bag2wav --input=audio.bag --output=audio.wav --input-audio-topic=/audio/audio")
	
	
def listener():

    rospy.init_node('command_listener', anonymous=True)
    rospy.Subscriber('voice_command', String, callback)

    rospy.spin()

if __name__ == '__main__':

    listener()

