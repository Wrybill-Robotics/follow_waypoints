#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from actionlib_msgs.msg import GoalID
from geometry_msgs.msg import PointStamped, PoseArray, PoseWithCovarianceStamped, Quaternion

class FollowWaypoints(Node):
    def __init__(self):
        # init ROS node
        super().__init__("follow_waypoints")
        self.get_logger().info("Starting Follow Waypoints node...")
        pass

def main(args=None):
    try:
        rclpy.init(args=args)
        node = FollowWaypoints()
        rclpy.spin(node)
        node.destroy_node()
    except KeyboardInterrupt:
        rclpy.shutdown()

if __name__ == "__main__":
    main()
