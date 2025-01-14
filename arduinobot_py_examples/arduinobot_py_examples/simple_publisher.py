import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__("simple_publisher")
        self.pub_ = self.create_publisher(String, "chatter", 10)
        self.counter_ = 0
        self.frequency_ = 1.0
        self.get_logger().info(f"Publisheing at {self.frequency_} Hz")
        self.timer_ = self.create_timer(self.frequency_, self.timer_callback)
    
    def timer_callback(self):
        msg = String()
        msg.data = f"Hello ROS2 - counter: {self.counter_}"
        self.pub_.publish(msg)
        self.counter_ += 1

def main():
    rclpy.init()
    node = SimplePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()