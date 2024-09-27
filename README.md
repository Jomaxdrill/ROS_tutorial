Project 0: Getting Started with Linux, ROS, Rviz2 and
Gazebo
Repository : https://github.com/Jomaxdrill/ROS_tutorial

This project is a tutorial to learn how to use ROS and Gazebo using the simulation robot of turtlebot3. 
## AUTHORS
jcrespo 121028099

## DEPENDENCIES and PACKAGES
python 3.11.7 or 3.8
(pip installer used)

## LIBRARIES
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

## GENERAL SETUP
-Verify you have ROS2 galatic distribution installed and also CMAKE necessary installations 
On command line run ```echo $ROS_DISTRO```
-Install previously the following packages and any additional in your linux distribution running on the terminal the command:
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
colcon build
```
- Source ROS (Package will be identified)

```sh
 source /opt/ros/galactic/setup.bash

```
-Run the gazebo environment (require to have the turtlebot3 ROS project and packages installed) check for: 

https://ros2-industrial-workshop.readthedocs.io/en/latest/_source/navigation/ROS2-Turtlebot.html

```sh
ros2 launch turtlebot3_gazebo empty_world.launch.py
```

- In other terminal locale the WORKSPACE_FOLDER ,source package to be identified. Do this for every new terminal you open.

```sh
cd ~\WORKSPACE_FOLDER
source install/setup.bash
```
## EXCECUTION TELEOPERATION
-Run the following script in other terminal and follow instructions in terminal while gazebo is open.
```sh
source /opt/ros/galactic/setup.bash
ros2 run turtlebot3_teleop teleop_keyboard
```
## EXCECUTION OPEN LOOP CONTROLLER
-Run the following script and see what displays in gazebo
```sh
ros2 run tb_control tb_openLoop
```
The following command runs the script tb_openLoop.py located in the tb_control folder. You will see the robot exceuting two movements or scenarios. One the velocity is constant. 
As soon the first scenario is finished the second scenario begins accelerating until reaching a top speed, maintaining constant top speed and after a while decreasing speed to reach zero.

![Screenshot 2024-09-27 155033](https://github.com/user-attachments/assets/e5333c9e-fb0c-47e1-82b1-3188c84d96b3)


This is all done in a settled time of 10 seconds for each scenario. You can change that modifying directly on script the constant value MAX_TIME.

![Settled max time](https://github.com/user-attachments/assets/a32a130f-1f73-4b28-83e4-5ed4fade4ccd)

You can use the parameter vel_x to a value as the show in the following example. By default is 0.1 if you don't specify the parameter.
```sh
ros2 run tb_control tb_openLoop --ros-args -p "vel_x:=0.2"
```
For any changes you do in the python file run:

```sh
cd ~\WORKSPACE_FOLDER
colcon build --packages-select tb_control
```
To reset the simulation also set the robot in the initial position by using the option 'Reset model poses' as shown here:

![Screenshot 2024-09-27 155156](https://github.com/user-attachments/assets/ceec41a6-7950-4ba8-be29-1adbb5928de4)


# Video links
### TurtleBot3 tele operation 
https://drive.google.com/file/d/1CEXyWKnralPQkr05YcF0xgmMEfWInOpl/view?usp=sharing
### TurtleBot3 open loop controller
https://drive.google.com/file/d/1TwJvgT9ib3v8p0MDkzqubbVuIIVubRgi/view?usp=sharing


