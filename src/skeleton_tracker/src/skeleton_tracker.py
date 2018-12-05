#!/usr/bin/env python
import numpy as np
import rospy
import sys
import tf
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

tol = 0.3
tol1 = 0.1
cmd_vel = Twist()
forward = -2.0
backward = -1.0
left = 0.28
right = -0.2
head = 0.465

rospy.init_node('skeleton_cmd')
listener = tf.TransformListener()
pub = rospy.Publisher('/RosAria/cmd_vel', Twist, queue_size=1)

sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')

previous_trans = Vector3()
#counter = 10
r = rospy.Rate(20)
while not rospy.is_shutdown():
    cmd_vel.linear.x = 0.0
    cmd_vel.angular.z = 0.0
    try:
        (trans, rot) = listener.lookupTransform('/head', '/openni_depth_frame', rospy.Time(0))
        print(trans)
        if trans != previous_trans:
            if trans[0] < right:
                print('right')
                cmd_vel.angular.z = -1.0
            elif trans[0] > left:
                print('left')
                cmd_vel.angular.z = 1.0

            if trans[2] < forward:
                print('forward')
                cmd_vel.linear.x = 1.0
            elif trans[2] > backward:
                print('backward')
                cmd_vel.linear.x = -1.0

        previous_trans = trans
        pub.publish(cmd_vel)

    except (tf.Exception, tf.ConnectivityException, tf.LookupException):
        rospy.logerr("tf error when looking up /openni_depth_frame and /torso")

    r.sleep()
