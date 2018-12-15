#! /usr/bin/env python


import os
import rospy
from std_msgs.msg import String
import time

def callback(data):
    if data.data == "generate":
	os.system("ffmpeg -y -i audio.wav  -r 30 -i video.mp4  -filter:a aresample=async=1 -c:a flac -c:v copy av.mkv")
	time.sleep(5)
	video_move = "av.mkv " + video_dir
	os.system(video_move)

def listener():

    rospy.init_node('video_combine', anonymous=True)

    rospy.Subscriber('voice_command', String, callback)
    rospy.spin()


home = os.getenv("HOME")
video_dir = home+'/catkin_ws/recorded_video/av.mkv'
if __name__ == '__main__':
    listener()
