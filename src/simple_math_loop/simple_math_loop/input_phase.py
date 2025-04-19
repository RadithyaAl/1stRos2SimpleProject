import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class MathInput(Node):
    def __init__(self):
        super().__init__('math_input_phase')

        # Subscribe to input topic
        self.check_last_value = self.create_subscription(Int32, 'maths3', self.phase1_callback, 10)

        # Publisher for output
        self.initial_value = self.create_publisher(Int32, 'maths', 10)

        self.x = 0
        self.received_first_value = False  # Flag to track if x has been initialized

        # Timer to kick-start the loop
        self.sent_first = False
        self.timer = self.create_timer(1.0, self.start_loop)

    def start_loop(self):
        if not self.sent_first:
            msg = Int32()
            msg.data = 0
            self.initial_value.publish(msg)
            self.get_logger().info('🌟 Starting the loop with: 0')
            self.sent_first = True  # prevent sending it again

    def phase1_callback(self, phase2_value):
        if not self.received_first_value:
            self.x = phase2_value.data
            self.received_first_value = True

        if self.x >= 20:
            self.x = 0
        else:
            self.x += 2

        math_phase1 = Int32()
        math_phase1.data = self.x
        self.initial_value.publish(math_phase1)

        self.get_logger().info(f"Phase2 heard: {phase2_value.data}")
        self.get_logger().info(f"Phase1 publishing: {math_phase1.data}")


def main(args=None):
    rclpy.init(args=args)
    mathinput = MathInput()
    rclpy.spin(mathinput)
    mathinput.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
