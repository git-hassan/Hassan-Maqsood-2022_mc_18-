import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time


class TriangleTurtle(Node):
    def __init__(self):
        super().__init__('triangle_turtle')
        self.publisher_ = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)
        self.step = 0
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        if self.step % 2 == 0:
            msg.linear.x = 2.0
            msg.angular.z = 0.0
        else:
            msg.linear.x = 0.0
            msg.angular.z = 4.188
        self.publisher_.publish(msg)
        self.step += 1


def main(args=None):
    rclpy.init(args=args)
    node = TriangleTurtle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()