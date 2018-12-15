#!/usr/bin/env python
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
import tf

rospy.init_node('move_robot_node')

listener = tf.TransformListener()

r = rospy.Rate(1)

right_low = -0.2
right_high = -0.9
left_low = 0.2
left_high = 0.9


def move_base_client():

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    rospy.loginfo("Waiting for move_base")
    client.wait_for_server()

    try:
        (trans, rot) = listener.lookupTransform('/torso', '/openni_depth_frame', rospy.Time(0))
        print(trans)
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "base_link"
        goal.target_pose.header.stamp = rospy.Time.now()
        if trans[0] < right_low and trans[0] > right_high:
            goal.target_pose.pose.position.x = 0.2
        elif trans[0] > left_low and trans[0] < right_high:
            goal.target_pose.pose.position.x = -0.2
        else:
            goal.target_pose.pose.position.x = 0.0
        # goal.target_pose.pose.position.x = -trans[0]
        # goal.target_pose.pose.position.y = trans[1]
        goal.target_pose.pose.position.z = trans[2]
        goal.target_pose.pose.orientation.w = 1.0

        client.send_goal(goal)
        wait = client.wait_for_result()
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            return client.get_result()

    except (tf.Exception, tf.ConnectivityException, tf.LookupException):
        rospy.logerr("tf error when looking up /openni_depth_frame and /torso")


if __name__ == "__main__":
    while not rospy.is_shutdown():
        try:
            result = move_base_client()
            if result:
                rospy.loginfo("Following target individual!")

        except rospy.ROSInterruptException:
            rospy.loginfo("Process terminated!")

        r.sleep()

