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

    def phase1_callback(self, math_phase3):
        if not self.received_first_value:
            self.x = math_phase3.data
            self.received_first_value = True

        if self.x >= 20:
            self.x = 0


        math_phase1 = Int32()
        math_phase1.data = self.x
        self.initial_value.publish(math_phase1)

        self.get_logger().info(f"phase2 hearing : {math_phase3.data}")
        self.get_logger().info(f"phase1 publishing : {math_phase1.data}")


def main(args=None):
    rclpy.init(args=args)
    mathinput = MathInput()
    rclpy.spin(mathinput)
    mathinput.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
