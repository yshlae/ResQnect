import time
import json
import os
from datetime import datetime

# Volunteer class
class Volunteer:
    def __init__(self, name, v_type, available):
        self.name = name
        self.v_type = v_type
        self.available = available

    def __str__(self):
        return f"{self.name} ({self.v_type}) - Available: {'Yes' if self.available else 'No'}"

    def to_dict(self):
        return {"name": self.name, "v_type": self.v_type, "available": self.available}

# Resource class
class Resource:
    def __init__(self, r_type, quantity):
        self.r_type = r_type
        self.quantity = quantity

    def __str__(self):
        return f"{self.r_type} - Quantity: {self.quantity}"

    def to_dict(self):
        return {"r_type": self.r_type, "quantity": self.quantity}

# Volunteer Manager
class VolunteerManager:
    def __init__(self):
        self.volunteers = []
        self.load_volunteers()

    def menu(self):
        while True:
            print("\n" + "=" * 50)
            print("Volunteer Management")
            print("=" * 50)
            print("1. Add a Volunteer")
            print("2. View Volunteers")
            print("3. Update Volunteer Availability")
            print("4. Back to Main Menu")
            option = input("Choose an option: ")

            if option == "1":
                self.add_volunteer()
            elif option == "2":
                self.view_volunteers()
            elif option == "3":
                self.update_volunteer_availability()
            elif option == "4":
                break
            else:
                print("Invalid option. Please try again.")

    def add_volunteer(self):
        print("\n=== Add a New Volunteer ===")
        name = input("Enter volunteer name: ")
        v_type = input("Enter volunteer type (medical/rescue/general): ")
        available = input("Is the volunteer available? (yes/no): ").strip().lower() == 'yes'
        self.volunteers.append(Volunteer(name, v_type, available))
        self.save_volunteers()
        print(f"Volunteer '{name}' added successfully!")

    def view_volunteers(self):
        print("\n=== List of Volunteers ===")
        if not self.volunteers:
            print("No volunteers available.")
        else:
            for volunteer in self.volunteers:
                print(volunteer)

    def update_volunteer_availability(self):
        name = input("Enter volunteer name to update availability: ")
        for volunteer in self.volunteers:
            if volunteer.name.lower() == name.lower():
                available = input("Is the volunteer available? (yes/no): ").strip().lower() == 'yes'
                volunteer.available = available
                self.save_volunteers()
                print(f"Availability for '{name}' updated!")
                return
        print("Volunteer not found.")

    def save_volunteers(self):
        data = [volunteer.to_dict() for volunteer in self.volunteers]
        with open("volunteers.json", "w") as f:
            json.dump(data, f)

    def load_volunteers(self):
        if os.path.exists("volunteers.json"):
            with open("volunteers.json", "r") as f:
                data = json.load(f)
                self.volunteers = [Volunteer(**v) for v in data]

# Resource Manager
class ResourceManager:
    def __init__(self):
        self.resources = {}
        self.load_resources()

    def menu(self):
        while True:
            print("\n" + "=" * 50)
            print("Resource Management")
            print("=" * 50)
            print("1. Add Resources")
            print("2. View Available Resources")
            print("3. Update Resource Quantities")
            print("4. Back to Main Menu")
            option = input("Choose an option: ")

            if option == "1":
                self.add_resource()
            elif option == "2":
                self.view_resources()
            elif option == "3":
                self.update_resource_quantity()
            elif option == "4":
                break
            else:
                print("Invalid option. Please try again.")

    def add_resource(self):
        print("\n=== Add a New Resource ===")
        r_type = input("Enter resource type (food, water, clothes, etc.): ")
        quantity = int(input("Enter quantity: "))
        self.resources[r_type] = Resource(r_type, quantity)
        self.save_resources()
        print(f"Resource '{r_type}' added successfully!")

    def view_resources(self):
        print("\n=== Available Resources ===")
        if not self.resources:
            print("No resources available.")
        else:
            for resource in self.resources.values():
                print(resource)

    def update_resource_quantity(self):
        r_type = input("Enter resource type to update quantity: ")
        if r_type in self.resources:
            quantity = int(input("Enter new quantity: "))
            self.resources[r_type].quantity = quantity
            self.save_resources()
            print(f"Quantity for '{r_type}' updated!")
        else:
            print("Resource not found.")

    def save_resources(self):
        data = {key: res.to_dict() for key, res in self.resources.items()}
        with open("resources.json", "w") as f:
            json.dump(data, f)

    def load_resources(self):
        if os.path.exists("resources.json"):
            with open("resources.json", "r") as f:
                data = json.load(f)
                self.resources = {k: Resource(**v) for k, v in data.items()}

# Disaster Response System
class DisasterResponseSystem:
    def __init__(self):
        self.volunteer_manager = VolunteerManager()
        self.resource_manager = ResourceManager()
        self.tasks = []

    def start(self):
        while True:
            print("\n" + "=" * 50)
            print("Disaster Response and Relief Management System")
            print("=" * 50)
            print("1. Volunteer Management")
            print("2. Resource Management")
            print("3. Task Assignment")
            print("4. Disaster Response Tracker")
            print("5. Response Time Reports")
            print("6. Exit")
            option = input("Choose an option: ")

            if option == "1":
                self.volunteer_manager.menu()
            elif option == "2":
                self.resource_manager.menu()
            elif option == "3":
                self.assign_task()
            elif option == "4":
                self.track_disaster_response()
            elif option == "5":
                self.generate_response_time_report()
            elif option == "6":
                print("Exiting the system. Prepare, Respond, Recover, Repeat!")
                break
            else:
                print("Invalid option. Please try again.")

    def assign_task(self):
        print("\n=== Task Assignment ===")
        task_type = input("Enter task type (rescue/medical/food distribution): ")
        volunteer_name = input("Enter volunteer name to assign the task to: ")

        volunteer = next((v for v in self.volunteer_manager.volunteers if v.name.lower() == volunteer_name.lower()), None)
        if volunteer and volunteer.available:
            task = {"task_type": task_type, "volunteer": volunteer.name, "status": "Assigned", "assigned_time": datetime.now(), "completion_time": None}
            self.tasks.append(task)
            print(f"Task '{task_type}' has been assigned to {volunteer.name}.")
        else:
            print("Volunteer not found or unavailable.")

    def track_disaster_response(self):
        print("\n=== Disaster Response Tracker ===")
        if not self.tasks:
            print("No tasks available to track.")
            return
        
        print("\nCurrent Tasks and Status Updates:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. Task: {task['task_type']}, Volunteer: {task['volunteer']}, Status: {task['status']}")
        
        task_index = int(input("Enter the task number to update its status, or 0 to go back: "))
        
        if task_index == 0:
            return
        elif 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            new_status = input("Enter new status: ")
            task['status'] = new_status

            # Record completion time when task is marked as "Completed"
            if new_status.lower() == 'completed' and task['completion_time'] is None:
                task['completion_time'] = datetime.now()  # Set the exact time of completion
            
            print(f"Task status updated to '{new_status}'.")
        else:
            print("Invalid task number.")

    def generate_response_time_report(self):
        print("\n=== Response Time Report ===")
        for task in self.tasks:
            if task['completion_time'] is not None:
               time_taken = task['completion_time'] - task['assigned_time']
               # Convert the time_taken to a formatted string in hh:mm:ss
               time_taken_seconds = time_taken.total_seconds()
               hours = int(time_taken_seconds // 3600)
               minutes = int((time_taken_seconds % 3600) // 60)
               seconds = int(time_taken_seconds % 60)
               response_time_str = f"{hours:02}:{minutes:02}:{seconds:02}"

               print(f"Task: {task['task_type']} | Volunteer: {task['volunteer']} | Response Time: {response_time_str}")
            else:
               print(f"Task: {task['task_type']} | Volunteer: {task['volunteer']} | Status: Pending")

# Initialize and start the system
if __name__ == "__main__":
    system = DisasterResponseSystem()
    system.start()
