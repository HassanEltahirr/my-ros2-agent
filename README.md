
---

## 🏁 Getting Started

### 1. **Clone the Repo**

```sh
git clone <your-repo-url>
cd ros2_ws
```

### 2. **Install Dependencies**

- ROS 2 (Humble or later)
- Python 3.10+
- [crewai](https://pypi.org/project/crewai/)
- OpenAI API key (set `OPENAI_API_KEY` in your environment)

### 3. **Build the Workspace**

```sh
colcon build
source install/setup.bash
```

### 4. **Run the Nodes**

**Terminal 1:** (Agent node)
```sh
ros2 run crew_agent crew_agent_node
```

**Terminal 2:** (Manager node)
```sh
ros2 run crew_agent manager_node
```

### 5. **Assign Tasks**

- In the manager node terminal, type a task and press Enter.
- Watch as the Assistant narrates the process and the Manager reviews it.

---

## 🧩 Example Output

---

## 🌟 Extending the Project

- Add more agents (e.g., Inspector, DeliveryBot, BackupBot)
- Integrate with real robots or Gazebo simulation
- Build a web dashboard or add voice input
- Implement analytics and learning from feedback

---

## 📄 License

[MIT License](LICENSE)

---

## 🤝 Contributing

Pull requests and feature ideas are welcome!  
Open an issue to discuss your vision.

---

## 🙏 Acknowledgements

- [ROS 2](https://docs.ros.org/)
- [CrewAI](https://pypi.org/project/crewai/)
- [OpenAI](https://platform.openai.com/)

---
