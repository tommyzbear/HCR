cmake_minimum_required(VERSION 2.8.3)
project(rosaria_keyboard)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  rospy
)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES rosaria_keyboard
#  CATKIN_DEPENDS geometry_msgs.msg rospy
#  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
