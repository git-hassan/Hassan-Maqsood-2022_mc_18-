import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import FollowWaypoints
from geometry_msgs.msg import PoseStamped

class WaypointNavigator(Node):
    def __init__(self):
        super().__init__('waypoint_navigator')
        self._client = ActionClient(self, FollowWaypoints, 'follow_waypoints')
        self.total_waypoints = 0

    def send_waypoints(self, waypoints):
        self.total_waypoints = len(waypoints)
        self.get_logger().info('Waiting for Nav2 FollowWaypoints action server...')
        self._client.wait_for_server()

        goal_msg = FollowWaypoints.Goal()
        goal_msg.poses = waypoints

        self.get_logger().info(f'--- Mission Started: {self.total_waypoints} Waypoints ---')
        
        send_goal_future = self._client.send_goal_async(
            goal_msg, 
            feedback_callback=self.feedback_callback
        )
        
        rclpy.spin_until_future_complete(self, send_goal_future)
        goal_handle = send_goal_future.result()

        if not goal_handle.accepted:
            self.get_logger().error('Goal rejected by the Nav2 server!')
            return

        self.get_logger().info('Goal accepted. Robot is now moving...')
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        
        self.get_logger().info('SUCCESS: All waypoints reached! Mission Complete.')

    def feedback_callback(self, feedback_msg):
        current = feedback_msg.feedback.current_waypoint
        remaining = self.total_waypoints - current - 1
        self.get_logger().info(f'Navigating to Waypoint #{current + 1} | Waypoints remaining: {remaining}')

def make_pose(x, y, yaw_w):
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.pose.position.x = float(x)
    pose.pose.position.y = float(y)
    pose.pose.position.z = 0.0
    pose.pose.orientation.z = 0.0
    pose.pose.orientation.w = float(yaw_w)
    return pose

def main(args=None):
    rclpy.init(args=args)
    navigator = WaypointNavigator()
    
    # Updated with your specific AMCL pose coordinates
    waypoints = [
        make_pose(2.593, -0.667, 0.989),  # Waypoint 1
        make_pose(3.967,  1.302, 1.000),  # Waypoint 2
        make_pose(2.355,  2.319, 1.000),  # Waypoint 3
        make_pose(0.940,  1.003, 1.000),  # Waypoint 4
        make_pose(0.013,  0.064, 1.000),  # Waypoint 5 (Origin)
    ]
    
    navigator.send_waypoints(waypoints)
    navigator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
