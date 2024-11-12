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

1. **Classes and Objects (OOP Basics)**
   - The `Volunteer` and `Resource` classes represent individual volunteers and resources.
   - `VolunteerManager` and `ResourceManager` classes manage groups of volunteers and resources, handling actions like adding, viewing, or updating entries.
   - The `DisasterResponseSystem` class brings everything together, managing volunteers, resources, tasks, and tracking responses.

2. **Data Saving and Loading (JSON and File Handling)**
   - **Data Persistence:** When a volunteer or resource is added or updated, their information is saved to a file (`volunteers.json` or `resources.json`). This ensures data persistence, so it remains available even if the program is closed and reopened.
   - **Loading Data:** On startup, the system checks if the JSON files exist and loads the data, saving the user from having to re-enter information every time.

3. **Looping and User Input Handling**
   - **Main Menu:** The `DisasterResponseSystem` class utilizes a loop to display a main menu, allowing the user to choose actions like managing volunteers, managing resources, assigning tasks, tracking responses, viewing reports, or exiting the program.
   - **Submenus:** Within the `VolunteerManager` and `ResourceManager` classes, submenus offer additional options (like adding, viewing, or updating records). `while True` loops in these sections enable continuous navigation until the user chooses to go back.

4. **User Input and Simple Logic**
   - **Getting User Input:** The system uses `input()` to gather details such as volunteer names, resource types, and quantities.
   - **Condition Checking:** `if` statements handle various options based on user input, providing a prompt to re-enter if the input is invalid.
   - **Updating Data:** For instance, updating a volunteer's availability involves finding the volunteer by name, modifying their status, and saving the revised data back to the file.

5. **Printing and Formatting Strings**
   - **`__str__` Method:** The `__str__` method in `Volunteer` and `Resource` classes customizes object printing, making volunteer availability and resource quantity display in a clean, readable format.
   - **Formatted Strings:** F-strings (`f"Task '{task_type}' has been assigned to {volunteer.name}."`) add clarity to outputs, creating dynamic, readable messages.

6. **Lists and Dictionaries**
   - **Lists:** Volunteers are stored in a list (`self.volunteers`), allowing easy addition and removal.
   - **Dictionaries:** Resources are stored in a dictionary (`self.resources`) where each resource type (like "food" or "water") serves as a key, and its quantity as the value. This setup allows quick updating of resource quantities.

7. **Task Assignment and Tracking**
   - **Assigning Tasks:** Users can assign tasks (e.g., medical aid, food distribution) to available volunteers.
   - **Tracking Tasks:** Assigned tasks are recorded in a list, and their statuses (e.g., “Assigned” or “Completed”) can be updated.
   - **Response Tracking:** This feature monitors each volunteer's assigned tasks and their status, enhancing real-time response tracking.

### Integration with SDG 🌍
<div align="center">
  <img src="https://github.com/yshlae/ResQnect/blob/main/images/SDG%20Goal%2011.jpg" alt="SDG Goal 11" width="500">
</div>

This project aligns with **Sustainable Development Goal (SDG) 11** by promoting **sustainable, resilient, and inclusive urban planning and management**. The system's core functionality supports communities in effectively managing volunteers, resources, and responses to minimize disaster impacts.

### Running the Program 👩‍💻
To run the ResQnect system, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/yshlae/ResQnect.git
