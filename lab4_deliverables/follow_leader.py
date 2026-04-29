import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn
import math

class FollowLeader(Node):
    def __init__(self):
        super().__init__('follow_leader')
        self.leader_pose = None
        self.follower_pose = None

        self.cli = self.create_client(Spawn, '/spawn')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /spawn service...')
        req = Spawn.Request()
        req.x = 2.0
        req.y = 2.0
        req.theta = 0.0
        req.name = 'turtle2'
        self.cli.call_async(req)

        self.leader_sub = self.create_subscription(
            Pose, '/turtle1/pose', self.leader_callback, 10)
        self.follower_sub = self.create_subscription(
            Pose, '/turtle2/pose', self.follower_callback, 10)
        self.cmd_pub = self.create_publisher(
            Twist, '/turtle2/cmd_vel', 10)

        self.timer = self.create_timer(0.1, self.control_loop)

    def leader_callback(self, msg):
        self.leader_pose = msg

    def follower_callback(self, msg):
        self.follower_pose = msg

    def control_loop(self):
        if self.leader_pose is None or self.follower_pose is None:
            return

        dx = self.leader_pose.x - self.follower_pose.x
        dy = self.leader_pose.y - self.follower_pose.y
        distance = math.sqrt(dx**2 + dy**2)
        angle_to_leader = math.atan2(dy, dx)
        angle_diff = angle_to_leader - self.follower_pose.theta

        while angle_diff > math.pi:
            angle_diff -= 2 * math.pi
        while angle_diff < -math.pi:
            angle_diff += 2 * math.pi

        cmd = Twist()
        if distance > 1.0:
            cmd.linear.x = min(1.5 * distance, 3.0)
            cmd.angular.z = 4.0 * angle_diff
        self.cmd_pub.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = FollowLeader()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
