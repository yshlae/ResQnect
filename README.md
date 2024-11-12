<div align="center">
  <img src="https://github.com/yshlae/ResQnect/blob/main/images/resqnect%20logo.png" alt="ResQnect Logo" width="240" height="240">
  
  <h1>ResQnect</h1>
  
  <h3>🚨 Prepare, Respond, Recover, Repeat. 🚨 <br>
  A disaster response management system for communities. Built for support, made to connect.</h3>
  
  <p><b>IT 2104</b><br>
  <a href="https://github.com/yshlae">Banaag, Ashley Mae R.</a></p>
  
  <hr class="w-48 h-1 mx-auto my-4 bg-gray-100 border-0 rounded md:my-10 dark:bg-gray-700">
</div>

<details>
  <summary>Table of Contents</summary>
  
  1. [Project Overview](#project-overview)  
  2. [Application of Python Concepts](#application-of-python-concepts)  
  3. [Integration with SDG](#integration-with-sdg)  
  4. [Running the Program](#running-the-program)  

</details>

---

### Project Overview 🔍
**𝘙𝘦𝘴𝘘𝘯𝘦𝘤𝘵** is a comprehensive disaster response management system designed to help local governments and relief organizations effectively coordinate emergency response activities. By providing streamlined volunteer management and effective tracking of essential resources like food and medical supplies, the system enables communities to be better prepared for emergencies. The main objective of this system is to assist communities prepare for, respond to, and recover from calamities. 

### Application of Python Concepts 🐍
In developing ResQnect, several Python concepts and libraries were applied to achieve efficient and scalable performance, including:

- **Classes and Objects (OOP Basics)**  📚
  - I created the `Volunteer` and `Resource` classes to represent individual volunteers and resources.
  - For managing these groups, I implemented `VolunteerManager` and `ResourceManager` classes to handle actions like adding, viewing, or updating records.
  - The `DisasterResponseSystem` class serves as the main controller, integrating volunteer and resource management, task assignment, and response tracking under one system.

- **Data Saving and Loading (JSON and File Handling)**  🗂️
  - *Saving Data:* Whenever a new volunteer or resource is added or updated, their information is stored in JSON files (`volunteers.json` or `resources.json`). This ensures data remains available, even if the program is closed and reopened.
  - *Loading Data:* On startup, the system checks for existing JSON files to load saved data, eliminating the need to re-enter information each time.

- **Looping and User Input Handling**  🔁
  - *Main Menu:* In the `DisasterResponseSystem` class, I created a loop to display the main menu, where users can choose options like managing volunteers, resources, tasks, viewing reports, or exiting.
  - *Submenus:* Within `VolunteerManager` and `ResourceManager`, submenus provide more detailed options like adding, viewing, and updating records. I used `while True` loops for seamless navigation until the user chooses to exit.

- **User Input and Logical Processing**  🗃️
  - *Getting User Input:* The program uses `input()` to gather details like volunteer names, resource types, and quantities.
  - *Condition Checking:* I used `if` statements to manage user choices, prompting re-entry when inputs are invalid.
  - *Data Updating:* For example, updating a volunteer’s availability status involves finding the specific volunteer, modifying their data, and saving the updated list back to the file.

- **Printing and Formatting Strings**  🗳️
  - `__str__` *Method:* In `Volunteer` and `Resource` classes, the `__str__` method customizes how information displays, making volunteer and resource data easy to read.
  - *Formatted Strings:* I used f-strings (e.g., `f"Task '{task_type}' has been assigned to {volunteer.name}.") to make output messages clear and dynamic.

- **Lists and Dictionaries**  📋
  - *Lists for Volunteer Storage:* All volunteers are stored in a list (`self.volunteers`), making it easy to add, remove, or iterate through them.
  - *Dictionaries for Resource Management:* Resources are organized in a dictionary (`self.resources`) with resource types as keys and quantities as values. This allows for quick lookups and updates.

- **Task Assignment and Tracking**  ⏱️
  - *Assigning Tasks:* Users can assign tasks (e.g., medical aid, food distribution) to available volunteers.
  - *Tracking Tasks:* Assigned tasks are saved in a list, allowing for status updates (e.g., “Assigned” to “Completed”).
  - *Response Tracking:* Each volunteer’s assigned tasks and their statuses are tracked, providing an overview of response efforts in real time.

### Integration with SDG 🌍
<div align="center">
  <img src="https://github.com/yshlae/ResQnect/blob/main/images/SDG%20Goal%2011.jpg" alt="SDG Goal 11" width="500">
</div>

**Sustainable Development Goal (SDG) 11: Sustainable Cities and Communities** aims to make cities and human settlements inclusive, safe, resilient, and sustainable. This goal focuses on improving urban planning, reducing the impact of natural disasters, and ensuring that communities are better prepared to respond to and recover from emergencies. **ResQnect** directly supports this goal by offering a digital solution that helps communities organize resources and manage volunteers during disaster response efforts.

This system contributes to SDG 11 in three key areas. First, it aids in **preparation** by allowing communities to track and store essential resources such as food, water, and medical supplies, ensuring quick mobilization when disaster strikes. The system's ability to maintain an updated inventory of resources helps communities be better prepared for emergencies. Second, during the **response and recovery** phases, it facilitates the assignment of tasks and the management of volunteers, ensuring that resources are deployed efficiently and volunteers can be quickly assigned to critical areas. Task tracking and real-time response monitoring ensure timely intervention in disaster-affected regions. Lastly, the system contributes to resilience building by allowing communities to track response times, resource usage, and volunteer deployment. This data helps communities improve their disaster response strategies over time.

### Running the Program 👩‍💻
To run the ResQnect system, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/yshlae/ResQnect.git
