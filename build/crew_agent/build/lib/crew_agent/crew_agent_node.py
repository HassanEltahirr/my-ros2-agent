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
        self.subscription = self.create_subscription(
            String,
            'manager/task_input',
            self.handle_user_task,
            10
        )
        self.get_logger().info("CrewAgentNode started.")
        # self.run_crew()  # REMOVE THIS LINE

    def handle_user_task(self, msg):
        user_task = msg.data
        self.get_logger().info(f"Received user task: {user_task}")

        # Create agents
        assistant = Agent(
            name="Assistant",
            role="Assistant",
            goal="Do the task assigned by the manager",
            backstory="A specialized robot designed to listen to the manager and execute the task."
        )
        manager = Agent(
            name="Manager",
            role="Manager",
            goal="Review the assistant's work and give feedback to the user and assistant",
            backstory="Your job is to review the task assigned by the user and the assistant's performance. Be specific about what was done well and what could be improved."
        )

        # Assistant does the task
        task1 = Task(
            description=(
                f"You are the Assistant. The manager has assigned you this task: '{user_task}'. "
                "As you perform the task, narrate your actions step by step, as if you are reporting live. "
                "For each step, specify exactly what you are doing, what items or tools you use, and any observations or challenges. "
                "List the types of items you handle (e.g., 'removed plastic bottles, paper, and food wrappers'), and mention any cleaning supplies or equipment you utilize. "
                "Be as explicit and detailed as possible, so the manager can fully understand your process."
            ),
            expected_output=(
                "A numbered, step-by-step description of how you completed the task, including time taken, actions performed, items handled, and tools or supplies used."
            ),
            agent=assistant
        )

        # Run the assistant's task first
        crew1 = Crew(agents=[assistant], tasks=[task1])
        results1 = crew1.kickoff()
        assistant_output = None
        for task_output in results1.tasks_output:
            if task_output.agent == "Assistant":
                assistant_output = task_output.raw
                msg_out = String()
                msg_out.data = f"\n=== Assistant's Process ===\n{assistant_output}\n"
                self.publisher_.publish(msg_out)
                self.get_logger().info(f"Published: {msg_out.data}")

        # Manager reviews the assistant's work
        if assistant_output:
            review_prompt = (
                f"The assistant was asked to: '{user_task}'.\n"
                f"The assistant responded with this detailed process: '{assistant_output}'.\n"
                "As the manager, review the assistant's work. Was the process thorough? Did the assistant communicate progress well? "
                "Give feedback and suggest areas for improvement."
            )
            task2 = Task(
                description=review_prompt,
                expected_output="Review and feedback provided.",
                agent=manager
            )
            crew2 = Crew(agents=[manager], tasks=[task2])
            results2 = crew2.kickoff()
            for task_output in results2.tasks_output:
                if task_output.agent == "Manager":
                    msg_out = String()
                    msg_out.data = f"\n=== Manager's Review ===\n{task_output.raw}\n"
                    self.publisher_.publish(msg_out)
                    self.get_logger().info(f"Published: {msg_out.data}")

    def run_crew(self):
        assistant = Agent(
            name="Assistant",
            role="Assistant",
            goal="Do the task assigned by the manager",
            backstory="A specialized robot designed to listen to the manager and execute the task."
        )

        manager = Agent(
            name="Manager of Assistant",
            role="Manager",
            goal="Review the task assigned by the user and assign it to the assistant",
            backstory="your job is to review the task assigned by the user and assign it to the assistant and give constructive criticism as if you were there saying the good and the bad"
        )

        task1 = Task(
            description="User assigned task",
            expected_output="Do them successfully.",
            agent=assistant
        )

        task2 = Task(
            description="review the assistant's performance",
            expected_output="do a review and give a feedback to the assistant.",
            agent=manager
        )

        crew = Crew(agents=[assistant, manager], tasks=[task1, task2])
        results = crew.kickoff()

        for task_output in results.tasks_output:
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

