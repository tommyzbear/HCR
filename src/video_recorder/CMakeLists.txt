cmake_minimum_required(VERSION 2.8.3)
project(video_recorder)

set(OpenCV_DIR /usr/share/OpenCV/)
find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  OpenCV
  cv_bridge
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES 
#  newrecording
#  CATKIN_DEPENDS rospy std_msgs
#  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)
