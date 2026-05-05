import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np

class LidarNavigator(Node):
    def __init__(self):
        super().__init__('lidar_navigator')

        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)

        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

        # Thresholds (in meters)
        self.front_threshold = 0.5
        self.side_threshold  = 0.4

        self.get_logger().info('LidarNavigator node started.')

    def scan_callback(self, msg):
        ranges = np.array(msg.ranges)

        # --- TODO 1: Clean data (replace inf/nan with large value) ---
        ranges = np.where(np.isfinite(ranges), ranges, 10.0)

        total = len(ranges)  # 360 for burger model

        # --- TODO 2: Define regions ---
        # Front: indices around 0° (last 15 + first 15 = 30 readings)
        front = np.concatenate([ranges[0:15], ranges[total-15:total]])
        # Left: indices around 90°
        left  = ranges[total//4 - 15 : total//4 + 15]
        # Right: indices around 270°
        right = ranges[3*total//4 - 15 : 3*total//4 + 15]

        front_dist = float(np.min(front))
        left_dist  = float(np.min(left))
        right_dist = float(np.min(right))

        self.get_logger().info(
            f'Front: {front_dist:.2f}  Left: {left_dist:.2f}  Right: {right_dist:.2f}')

        twist = Twist()

        # --- TODO 3: Obstacle logic ---
        if front_dist < self.front_threshold:   # obstacle in front

            twist.linear.x = 0.0               # stop forward motion

            # --- TODO 4: Turn toward side with larger clearance ---
            if left_dist > right_dist:          # left is clearer
                twist.angular.z =  0.5          # turn left (CCW)
            else:
                twist.angular.z = -0.5          # turn right (CW)

        else:
            # --- TODO 5: Forward motion with gentle wall-following ---
            twist.linear.x  = 0.15

            # Proportional wall-follow: try to keep ~0.5 m from left wall
            error = left_dist - 0.5
            twist.angular.z = -0.3 * error      # negative = steer right if too close

        self.publisher.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = LidarNavigator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
