from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    realsense_launch_dir = os.path.join(
        get_package_share_directory('realsense2_camera'), 'launch'
    )

    livox_launch_file = os.path.expanduser(
        '~/slam_ws/src/ws_livox/src/livox_ros_driver2/launch_ROS2/msg_MID360_launch.py'
    )

    rviz_config_file = os.path.expanduser(
        '~/slam_ws/rviz_configs/multisensor_config_1.rviz'
    )

    fisheye_launch_file = os.path.expanduser(
        '~/slam_ws/src/moonbotslam/launch/fisheye_cameras_launch.py'
    )

    return LaunchDescription([
        IncludeLaunchDescription(
           PythonLaunchDescriptionSource(
               os.path.join(realsense_launch_dir, 'rs_launch.py')
           )
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                livox_launch_file
            )
        ),

        # Hier das neue Fisheye-Launchfile includen, z.B. mit activate_rectification auf true
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(fisheye_launch_file),
            launch_arguments={'activate_rectification': 'true'}.items()
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_file],
            output='screen'
        )
    ])
