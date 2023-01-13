from launch import LaunchDescription
from launch_ros.actions import Node

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    joy_params = os.path.join(get_package_share_directory('mobile_rob'),'config','joystick.yaml')

    joy_node = Node(
            package='joy',
            executable='joy_node',
            parameters=[joy_params],
         )

    #used before nav2
    #teleop_node = Node(
    #        package='teleop_twist_joy', 
    #        executable='teleop_node',
    #        name = 'teleop_node',
    #        parameters=[joy_params],
    #        remappings=[('/cmd_vel', '/diff_cont/cmd_vel_unstamped')]
    #        )

    #used with nav2
    teleop_node = Node(
        package='teleop_twist_joy', 
        executable='teleop_node',
        name = 'teleop_node',
        parameters=[joy_params],
        remappings=[('/cmd_vel', '/cmd_vel_joy')]
        )

    return LaunchDescription([
        joy_node,  
        teleop_node    
    ])


    #to use on the robot:
    # ros2 launch mobile_rob launch_sim.launch.py
    #in another terminal
    # ros2 launch mobile_rob joystick.launch.py
    # to see the topic
    # ros2 topic echo /diff_cont/cmd_vel_unstamped