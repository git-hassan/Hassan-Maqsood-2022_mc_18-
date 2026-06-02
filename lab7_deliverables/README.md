# Lab 7: Autonomous Navigation with Nav2 and Multi-Waypoint Mission Planning

## 1. Introduction & Methodology
This lab session focuses on setting up autonomous navigation for a TurtleBot3 using the ROS 2 Nav2 stack. Using a static occupancy map generated in previous SLAM labs, AMCL was utilized to localize the robot. Following successful localization, autonomous mission planning was achieved through both RViz interfaces and custom Python nodes communicating with the `FollowWaypoints` action server.

## 2. Multi-Waypoint Mission (Task 2)
The robot successfully completed a sequential patrol through the following coordinates:

| Waypoint # | X (m) | Y (m) | Z (m) | Yaw (w) | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 2.593 | -0.667 | 0.0 | 0.989 | Initial exploration point |
| 2 | 3.967 | 1.302 | 0.0 | 1.000 | Top right corridor |
| 3 | 2.355 | 2.319 | 0.0 | 1.000 | Upper section |
| 4 | 0.940 | 1.003 | 0.0 | 1.000 | Middle transition point |
| 5 | 0.013 | 0.064 | 0.0 | 1.000 | Return to origin |

## 3. Costmap Observations (Task 4)
* **Global Costmap (`/global_costmap/costmap`):** Primarily uses the static map loaded by the map server to plan the initial route from the robot's current pose to the final goal. It represents static obstacles and their inflation bounds.
* **Local Costmap (`/local_costmap/costmap`):** Uses real-time LiDAR data to create a rolling window around the robot. This allows the DWB controller to avoid dynamic, unmapped obstacles in its immediate path while trying to stick to the global plan. 

## 4. Navigation Recovery Behaviors (Task 5)
When a dynamic obstacle (a box) was inserted into the robot's path in Gazebo, Nav2's local controller initially attempted to steer around it. When the path was fully blocked, the robot engaged its recovery servers.
* **Observed Actions:** The robot stopped and executed a `Spin` recovery maneuver to re-scan the environment with its LiDAR. If no clear path was found, a `Backup` recovery was triggered. 
* **Handling Server:** This behavior is handled by the `recoveries_server` (Behavior Server) visible in `rqt_graph`.

## 5. Conclusion
This lab highlighted the transition from environment mapping to autonomous task execution. While SLAM (Lab 5) focused strictly on sensor data integration to build a spatial representation, Navigation (Lab 7) leverages that map for active decision-making and path planning. A key challenge faced was initial collisions due to poor localization, which was resolved by providing an accurate 2D Pose Estimate and teleoperating the robot to allow the AMCL particle cloud to converge before dispatching waypoints.

## 6. Single Goal Navigation (Task 1)
Using the RViz Nav2 Goal tool, three separate navigation goals were dispatched to test basic path planning and local costmap obstacle avoidance.

| Goal | Start Pose (x, y, w) | End Pose (x, y, w) | Status (Success/Recovery) |
| :--- | :--- | :--- | :--- |
| 1 | (0.013, 0.064, 1.000) | (1.550, 0.750, 0.707) | Success (Direct Path) |
| 2 | (1.550, 0.750, 0.707) | (2.593, -0.667, 0.989) | Success (Minor path adjustment) |
| 3 | (2.593, -0.667, 0.989) | (3.967, 1.302, 1.000) | Recovery (Spin executed), then Success |
