import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32

class MathPhase2(Node):
    def __init__(self):
        super().__init__('math_second_phase')
        self.phase2_listener = self.create_subscription(Int32, 'maths2', self.phase2_callback ,10)
        self.phase2_publisher = self.create_publisher(Int32, 'maths3', 10)

    def phase2_callback(self, phase1_value):
        phase2_value = Int32()
        phase2_value.data = phase1_value.data + 1

        self.phase2_publisher.publish(phase2_value)
        self.get_logger().info(f"Phase1 Received: {phase1_value.data} | Published: {phase2_value.data}")


def main(args=None):
    rclpy.init(args=args)
    node = MathPhase2()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
