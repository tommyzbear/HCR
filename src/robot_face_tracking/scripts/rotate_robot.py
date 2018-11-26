#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Twist
msg=Twist()
def callback(data):
    #pub=rospy.Publisher('cmd_vel',Twist,queue_size=10)
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

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('rotate_robot', anonymous=True)

    rospy.Subscriber('rotation_angle', Float32, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
	rospy.init_node('rotate_robot', anonymous=True)
	pub=rospy.Publisher('/RosAria/cmd_vel',Twist,queue_size=10)
	#rospy.Subscriber('rotation_angle', Float32, callback)
	#rospy.Subscriber('velocity', Float32, vel_callback)
	rospy.Subscriber('movement', Float32MultiArray, callback)	
	rospy.spin()
    
