#!/usr/bin/env python
import csv
import rospy
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import Quaternion
from std_msgs.msg import UInt16

import tf

tol = 0.4
tol1= 0.1 #0.3
foward = -0.1
backward = 0 #-0.23
left = 0.4714
right = 0.4609
angle = 90

rospy.init_node('quat2rpy')
listener = tf.TransformListener()
pub = rospy.Publisher('/servo', UInt16, queue_size=1)

r = rospy.Rate(10)

while not rospy.is_shutdown():
    try:
        (trans,rot) = listener.lookupTransform('/right_elbow','/openni_depth_frame',  rospy.Time(0))
        (trans1,rot1) = listener.lookupTransform('/right_hand','/openni_depth_frame',  rospy.Time(0))
        
        (trans2,rot2) = listener.lookupTransform('/left_elbow','/openni_depth_frame',  rospy.Time(0))
        (trans3,rot3) = listener.lookupTransform('/left_hand','/openni_depth_frame',  rospy.Time(0))
        
        euler = tf.transformations.euler_from_quaternion(rot)
        euler1 = tf.transformations.euler_from_quaternion(rot1)
        euler2 = tf.transformations.euler_from_quaternion(rot2)
        euler3 = tf.transformations.euler_from_quaternion(rot3)
        
        print(euler[1],euler2[1], angle) 
        #print(trans1)
        #print(euler2)
        #print(trans3)
 
        if (euler[1] > foward-tol) and (euler[1] < foward+tol):
        
            #cmd_vel.linear.x=1.0
            #print('RIGHT')
 	    angle=60
            
        elif (euler2[1] > backward-tol) and (euler2[1] < backward+tol): 
        
            #cmd_vel.linear.x=-1.0
            #print('LEFT')
            angle=120
	
        #elif (trans1[1] > left-tol1) and (trans1[1] < left+tol1):
        
            #cmd_vel.angular.z=1.0
            #print('CENTRE')
         #   angle=90
            
        #elif (trans3[1] > right-tol1) and (trans3[1] < right+tol1):
            
            #cmd_vel.angular.z=-1.0
            #print('CENTRE')
         #   angle=90        
	     
        else:
            angle=90 
	print(angle)

	pub.publish(angle) 
           
        r.sleep()
    except:
        pass




rospy.loginfo("COMPLETE")
