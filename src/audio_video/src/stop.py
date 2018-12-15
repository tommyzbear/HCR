#!/usr/bin/env python

import rospy
from std_msgs.msg import String


if __name__ == '__main__':
    try:
	pub = rospy.Publisher('voice_command', String, queue_size=1)
	rospy.init_node('voice_command', anonymous=True)
	stop_str = "stop"
	rospy.loginfo(stop_str)
	pub.publish(stop_str)

	rospy.spin()
    except rospy.ROSInterruptException:
	pass
