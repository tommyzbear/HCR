#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Twist
msg=Twist()
def callback(data):

    if(data.data[1]>30):
	msg.angular.z=30*0.0174533
    elif(data.data[1]<-30):
	msg.angular.z=-30*0.0174533
    else:
    	msg.angular.z=(data.data[1])*0.0174533

    msg.linear.x=data.data[0]
    rospy.loginfo(rospy.get_caller_id() + "Robot velocity: %f, Rotation Angle: %f", msg.linear.x, msg.angular.z)
    pub.publish(msg)

def listener():

    rospy.init_node('rotate_robot', anonymous=True)

    rospy.Subscriber('rotation_angle', Float32, callback)

    rospy.spin()

if __name__ == '__main__':
	rospy.init_node('rotate_robot', anonymous=True)
	pub=rospy.Publisher('/RosAria/cmd_vel',Twist,queue_size=10)
	rospy.Subscriber('movement', Float32MultiArray, callback)	
	rospy.spin()
    
