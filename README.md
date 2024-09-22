Project 0: Getting Started with Linux, ROS, Rviz2 and
Gazebo
Repository : https://github.com/Jomaxdrill/ROS_tutorial

## AUTHORS
jcrespo 121028099

## DEPENDENCIES and PACKAGES
python 3.11.7 or 3.8
(pip installer used)

## LIBRARIES
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
## INSTRUCTIONS

## EXECUTION
-Verify you have ROS2 galatic distribution installed and also CMAKE necessary installations 
On command line run ```echo $ROS_DISTRO```
-Install previously the following packages and any additional in your vlinux distribution running on the terminal the command:
    ```sudo apt install python3-colcon-common-extensions```

-Install all necessary dependencies and libraries with pip for insrtance. Recommended to run in your own python environment.

-Install and run plotjugger:

```sh
sudo apt install ros-$ROS_DISTRO-plotjuggler-ros
ros2 run plotjugger plotjugger
```

-In other terminal build the package:
```sh
cd ~\WORKSPACE_FOLDER
colcon build --packages-select tb_control
```
- Source ROS (Package will be identified)

```sh
 source /opt/ros/galactic/setup.bash

```
-Run the gazebo environment (require to have the turtlebot3 ROS project and packages installed) check for:

```sh
ros2 launch turtlebot3_gazebo empty_world.launch.py
```
- In other terminal locale Part02 folder ,build it and source package to be identified

```sh
cd ~\Part02
colcon build
source install/setup.bash
```

-Run the following script and see what displays in gazebo
```sh
ros2 run tb_control tb_openLoop
```
The following command runs the script tb_openLoop.py located in the tb_control folder.
# Video links
### TurtleBot3 tele operation 
https://drive.google.com/file/d/1CEXyWKnralPQkr05YcF0xgmMEfWInOpl/view?usp=sharing
### TurtleBot3 open loop controller
https://drive.google.com/file/d/1TwJvgT9ib3v8p0MDkzqubbVuIIVubRgi/view?usp=sharing


