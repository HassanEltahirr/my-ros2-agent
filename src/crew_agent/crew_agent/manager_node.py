import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ManagerNode(Node):
    def __init__(self):
        super().__init__('manager_node')
        self.publisher_ = self.create_publisher(String, 'manager/task_input', 10)
        self.get_logger().info("ManagerNode started.")
        self.timer = self.create_timer(0.5, self.get_user_input)
        self.waiting = False

    def get_user_input(self):
        if not self.waiting:
            self.waiting = True
            user_input = input("Enter a new task for the crew: ")
            msg = String()
            msg.data = user_input
            self.publisher_.publish(msg)
            self.get_logger().info(f"Sent task: {msg.data}")
            self.waiting = False
    

def main(args=None):
    rclpy.init(args=args)
    node = ManagerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()