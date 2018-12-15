cmake_minimum_required(VERSION 2.8.3)
project(filter_laser_scan)


find_package(catkin REQUIRED COMPONENTS
  rospy
  sensor_msgs
	roscpp
)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES filter_laser_scan
#  CATKIN_DEPENDS rospy sensor_msgs
#  DEPENDS system_lib
)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(laser_scan_filter src/laser_scan_filter.cpp)
target_link_libraries(laser_scan_filter ${catkin_LIBRARIES})
