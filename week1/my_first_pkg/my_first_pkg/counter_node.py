import rclpy
from rclpy.node import Node
import os


COUNTER_FILE = os.path.expanduser('~/ros2_ws_hassan/src/my_first_pkg/my_first_pkg/run_counter.txt')


class CounterNode(Node):
    def __init__(self):
        super().__init__('counter_node')

        count = 0
        if os.path.exists(COUNTER_FILE):
            with open(COUNTER_FILE, 'r') as f:
                try:
                    count = int(f.read().strip())
                except ValueError:
                    count = 0

        count += 1

        with open(COUNTER_FILE, 'w') as f:
            f.write(str(count))

        self.get_logger().info(f'Run count: {count}')


def main(args=None):
    rclpy.init(args=args)
    node = CounterNode()
    rclpy.spin_once(node, timeout_sec=0.1)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
