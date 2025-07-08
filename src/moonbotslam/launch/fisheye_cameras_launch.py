from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Fisheye Left Camera
        Node(
            package='v4l2_camera',
            executable='v4l2_camera_node',
            namespace='fisheye_left',
            name='v4l2_camera_node',
            parameters=[
                {'video_device': '/dev/video10'},
                {'image_size': [640, 480]},
                {'framerate': 15.0},
                {'camera_info_url': 'file:///home/moonbotslam/slam_ws/src/moonbotslam/config/fisheye_camera_left_intrinsics.yaml'},
                'src/moonbotslam/param/fisheye_camera_left_params.yaml',
            ],
            output='screen'
        ),
        
        # Fisheye Left image_proc
        #Node(
        #    package='image_proc',
        #    executable='image_proc',
        #    namespace='fisheye_left',
        #    name='image_proc_left',
        #    remappings=[
        #        ('image', 'image_raw'),
        #        ('camera_info', 'camera_info'),
        #        ('image_rect', 'image_rect')
        #    ],
        #    output='screen'
        #),
        
        # Fisheye Right Camera
        
        Node(
            package='v4l2_camera',
            executable='v4l2_camera_node',
            namespace='fisheye_right',
            name='v4l2_camera_node',
            parameters=[
                {'video_device': '/dev/video6'},
                {'image_size': [640, 480]},
                {'framerate': 15.0},
                {'camera_info_url': 'file:///home/moonbotslam/slam_ws/src/moonbotslam/config/fisheye_camera_right_intrinsics.yaml'},
                'src/moonbotslam/param/fisheye_camera_right_params.yaml',
            ],
            output='screen'
        ),
        
        # Fisheye Right image_proc
        #Node(
        #    package='image_proc',
        #    executable='image_proc',
        #    namespace='fisheye_right',
        #    name='image_proc_right',
        #    remappings=[
        #        ('image', 'image_raw'),
        #        ('camera_info', 'camera_info'),
        #        ('image_rect', 'image_rect')
        #    ],
        #    output='screen'
        #),
        
    ])
