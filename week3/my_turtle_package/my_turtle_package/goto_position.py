import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math


class GoToPosition(Node):
    def __init__(self):
        super().__init__('goto_position')
        self.publisher_ = self.create_publisher(Twist, '/turtle3/cmd_vel', 10)
        self.subscription = self.create_subscription(Pose, '/turtle3/pose', self.pose_callback, 10)

        self.declare_parameter('target_x', 8.0)
        self.declare_parameter('target_y', 8.0)

        self.current_x = 0.0
        self.current_y = 0.0
        self.current_theta = 0.0
        self.reached = False

    def pose_callback(self, msg):
        self.current_x = msg.x
        self.current_y = msg.y
        self.current_theta = msg.theta

        target_x = self.get_parameter('target_x').get_parameter_value().double_value
        target_y = self.get_parameter('target_y').get_parameter_value().double_value

        dist = math.sqrt((target_x - self.current_x) ** 2 +
                         (target_y - self.current_y) ** 2)

        angle_to_target = math.atan2(target_y - self.current_y,
                                     target_x - self.current_x)
        angle_error = angle_to_target - self.current_theta

        twist = Twist()

        if dist > 0.2:
            self.reached = False
            twist.linear.x = 1.5
            twist.angular.z = 2.0 * angle_error
        else:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            if not self.reached:
                self.get_logger().info('Reached target position')
                self.reached = True

        self.publisher_.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = GoToPosition()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()