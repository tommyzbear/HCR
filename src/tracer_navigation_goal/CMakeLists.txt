cmake_minimum_required(VERSION 2.8.3)
project(tracer_navigation_goal)


find_package(catkin REQUIRED COMPONENTS
  actionlib
  move_base_msgs
  roscpp
)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES tracer_navigation_goal
#  CATKIN_DEPENDS actionlib move_base_msgs roscpp
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

#add_executable(tracer_navigation_goal src/tracer_navigation_goal.cpp)
#target_link_libraries(tracer_navigation_goal ${catkin_LIBRARIES})
