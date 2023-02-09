# Autonomous Mobile Robot for sensible material transport

## The aim of the project

In a biological laboratory there’s the need to keep cell’s vials safe and to conserve them in a box containing liquid nitrogen
This box stands in a refrigerated room and it’s possible to move it around to bring the vials to scientists to perform experiments

This project has the aim to simulate a mobile robot which is able to transport these vials autonomously, avoiding possible obastcles, to a scientist workstation in a goal position

## Schematic view of the project

### Modeling the robot

* Definition of a Differential Drive Robot
* Combining URDF and .xacro to create the model

### Simulation

* ROS2 + GAZEBO + Rviz
* Spawning robot with all the sensors in Gazebo and Rviz

### Controlling

* Gazebo control
* ros2_control
* Teleoperation
* Final definition of the launch file

### Mapping & Localization

* ROS & SLAM
* Localization using SLAM
* Localization using AMCL

### Navigation

* NAV2 + GAZEBO
* NAV2 with AMCL
* Twist Mux
