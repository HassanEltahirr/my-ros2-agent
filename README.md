
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
<img width="1520" height="968" alt="image" src="https://github.com/user-attachments/assets/0208fde3-ec96-4f86-8962-9de2232b43fa" />
<img width="1940" height="988" alt="image" src="https://github.com/user-attachments/assets/aca52433-70b9-445e-97ca-a953272d103f" />
<img width="2060" height="766" alt="image" src="https://github.com/user-attachments/assets/cb6da1d6-a2be-4f70-ba8c-73165c53ac97" />

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
