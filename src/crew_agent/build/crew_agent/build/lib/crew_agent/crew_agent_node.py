import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from crewai import Agent, Task, Crew
import os

# Optional: put your key here if not using .env
# os.environ["OPENAI_API_KEY"] = "sk-..."

class CrewAgentNode(Node):
    def __init__(self):
        super().__init__('crew_agent_node')
        self.publisher_ = self.create_publisher(String, 'crew_output', 10)
        self.get_logger().info("CrewAgentNode started.")
        self.run_crew()

    def run_crew(self):
        loader = Agent(
            name="Loader",
            role="Loader Robot",
            goal="Pick up items",
            backstory="A specialized robot designed to pick up items."
        )

        deliverer = Agent(
            name="Deliverer",
            role="Delivery Robot",
            goal="Deliver items to destination",
            backstory="An autonomous robot for last-mile delivery."
        )

        task1 = Task(
            description="Pick up items from the warehouse",
            expected_output="Items picked successfully.",
            agent=loader
        )

        task2 = Task(
            description="Deliver items to the destination",
            expected_output="Items delivered successfully.",
            agent=deliverer
        )

        crew = Crew(agents=[loader, deliverer], tasks=[task1, task2])
        results = crew.kickoff()

        for task_output in results['tasks_output']:
            msg = String()
            msg.data = f"[{task_output.agent}] {task_output.raw}"
            self.publisher_.publish(msg)
            self.get_logger().info(f"Published: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = CrewAgentNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

