import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class MathPhase1(Node):
    def __init__(self):
        super().__init__('math_first_phase')

        # Subscribe to 'maths' topic
        self.phase1_listener = self.create_subscription(
            Int32,
            'maths',
            self.phase1_callback,
            10
        )

        # Publish to 'maths2' topic
        self.phase1_publisher = self.create_publisher(
            Int32,
            'maths2',
            10
        )

    def phase1_callback(self, math_phase1):
        # Create a new message
        phase1_value = Int32()
        phase1_value.data = math_phase1.data + 2

        # Publish the modified value
        self.phase1_publisher.publish(phase1_value)

        # Log the result
        self.get_logger().info(f"Phase1 Received: {math_phase1.data} | Published: {phase1_value.data}")


def main(args=None):
    rclpy.init(args=args)
    node = MathPhase1()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
