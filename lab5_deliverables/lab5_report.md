# Lab Manual 5 Report
## MCT-454L Mobile Robotics
**Name:** Hassan Maqsood
**Reg No:** 2022-MC-18

---

## Steps Followed

1. Installed TurtleBot3 and Gazebo packages via apt.
2. Configured TURTLEBOT3_MODEL=burger in ~/.bashrc.
3. Launched Gazebo simulation using turtlebot3_world.launch.py.
4. Launched RViz with Cartographer for real-time SLAM mapping.
5. Added LaserScan, TF, Odometry, Path, and Map plugins in RViz.
6. Set Fixed Frame to map in RViz Global Options.
7. Used teleop_keyboard to navigate the robot and build the map.
8. Recorded robot motion using ros2 bag record -a.
9. Saved the generated map using map_saver_cli.
10. Wrote and ran a cmd_vel publisher alternating between forward and stop every 2 seconds.
11. Identified /odom message type as nav_msgs/msg/Odometry and wrote a subscriber node.

---

## Task Observations

### Task 3: TF Frames
The TF tree shows the map frame as root, connected to odom, which connects to
base_footprint, then base_link. Wheel frames and sensor frames branch from base_link.
These frames represent the robot's kinematic chain and localization hierarchy.

### Task 4: Odometry Display
The odometry arrows in RViz update in real time showing the robot's position and
orientation as it moves. The arrows accumulate along the path traveled.

### Task 5: Discrepancies Between Expected and Simulated Motion
Simulated motion is ideal with no wheel slip or mechanical noise. A small drift in
odometry was observed over longer trajectories due to accumulated integration error.
In real hardware this drift would be significantly larger.

### Task 7: Return to (0,0,0)
The robot was driven back toward the origin by monitoring the /odom topic values
and adjusting direction using teleop until x, y values approached zero.

---

## Conclusion
This lab provided hands-on experience with Gazebo simulation and RViz visualization
using TurtleBot3 in ROS 2 Humble. I learned how to perform SLAM using Cartographer,
visualize sensor data including LiDAR, odometry, and TF frames in real time, record
bag files for playback, and write functional publisher and subscriber nodes for motion
control and odometry monitoring. The main challenge was managing multiple terminals
simultaneously and ensuring each was properly sourced before running ROS 2 commands.
