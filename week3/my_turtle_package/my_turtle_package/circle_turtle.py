import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CircleTurtle(Node):
    def __init__(self):
        super().__init__('circle_turtle')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = CircleTurtle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()