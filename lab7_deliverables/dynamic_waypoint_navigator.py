import rclpy
import sys
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import FollowWaypoints
from geometry_msgs.msg import PoseStamped

class WaypointNavigator(Node):
    def __init__(self):
        super().__init__('waypoint_navigator')
        self._client = ActionClient(self, FollowWaypoints, 'follow_waypoints')

    def send_waypoints(self, waypoints):
        self.get_logger().info('Waiting for FollowWaypoints action server...')
        self._client.wait_for_server()
        goal_msg = FollowWaypoints.Goal()
        goal_msg.poses = waypoints
        self.get_logger().info(f'Sending {len(waypoints)} waypoints...')
        send_goal_future = self._client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, send_goal_future)
        goal_handle = send_goal_future.result()
        if not goal_handle.accepted:
            self.get_logger().error('Goal rejected by server!')
            return
        self.get_logger().info('Goal accepted. Navigating...')
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        self.get_logger().info('All waypoints reached!')

def make_pose(x, y, yaw_w):
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.pose.position.x = float(x)
    pose.pose.position.y = float(y)
    pose.pose.position.z = 0.0
    pose.pose.orientation.z = float(yaw_w)
    pose.pose.orientation.w = 1.0
    return pose

def main(args=None):
    rclpy.init(args=args)
    navigator = WaypointNavigator()

    # Parse command line arguments
    # Usage: python3 dynamic_waypoint_navigator.py x1 y1 w1 x2 y2 w2 ...
    raw_args = sys.argv[1:]
    if len(raw_args) == 0 or len(raw_args) % 3 != 0:
        print('Usage: python3 dynamic_waypoint_navigator.py x1 y1 w1 x2 y2 w2 ...')
        print('Example: python3 dynamic_waypoint_navigator.py 0.5 0.0 1.0 1.0 0.5 1.0')
        return

    waypoints = []
    for i in range(0, len(raw_args), 3):
        x, y, w = raw_args[i], raw_args[i+1], raw_args[i+2]
        waypoints.append(make_pose(x, y, w))
        print(f'Waypoint {i//3 + 1}: x={x}, y={y}, w={w}')

    navigator.send_waypoints(waypoints)
    navigator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
