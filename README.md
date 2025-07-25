# SLAM Workspace

## Livox MID360 ROS 2 Setup – Quick Guide & Learnings

Successfully running the Livox MID360 on ROS 2 Humble using `livox_ros_driver2`.

### Key Steps

Livox Mid 360 does not start with just 9V, 12V is better (2A).

1. Install Livox Driver and SDK
   Under: https://github.com/Livox-SDK/livox_ros_driver2

2. **Find the sensor IP**:
   ```bash
   sudo nmap -sn 192.168.1.0/24

3. Update the config file in your driver with the host ip (ethernet port) and livox ip (from livox viewer or step 2)
     Remember to also change the config in the install path of the driver!

4. Fix RViz “Fixed Frame [livox_frame] does not exist” error:
      In a separate terminal:

      ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 base_link livox_frame

      Then set "Fixed Frame" in RViz to livox_frame.
