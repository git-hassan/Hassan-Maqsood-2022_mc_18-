# Lab 4: ROS 2 Launch, Rosbag, rqt_plot
**Student:** Hassan Maqsood | 2022-MC-18

## Approach
- Used ros2 launch to start turtlesim_node and turtle_teleop_key simultaneously
- Spawned turtle2 and implemented proportional control so turtle2 follows turtle1
- Recorded /turtle1/pose and /turtle1/cmd_vel with rosbag and replayed to verify
- Extracted trajectory data to CSV using ros2 topic echo
- Used rqt_plot to visualize linear.x and angular.z of /turtle1/cmd_vel in real time
