import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle
from disaster_response_system import DisasterResponseSystem
from datetime import datetime
import os

class DisasterResponseUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ResQnect")
        self.root.geometry("900x700")
        self.style = ThemedStyle(self.root)
        self.style.set_theme("clam")  
        self.bg_color = "#ffffff"  
        self.fg_color = "#000000" 
        self.accent_color = "#4335A7"  
        self.root.configure(bg=self.bg_color)

        self.system = DisasterResponseSystem()

        self.setup_styles()
        self.create_widgets()

        try:
            self.icon_image = tk.PhotoImage(file=r"C:\Users\Acer\Downloads\RESQNECT-removebg-preview.png") 
            self.root.iconphoto(False, self.icon_image)
        except Exception:
            print("Warning: Icon image not found. Proceeding without it.")

    def setup_styles(self):
        self.style.configure("Custom.TFrame", background=self.bg_color)
        self.style.configure("Custom.TLabel", background=self.bg_color, foreground=self.fg_color, font=("Helvetica", 10))
        self.style.configure("Custom.TButton", background=self.accent_color, foreground="#FFFFFF", font=("Helvetica", 10))
        
        self.style.configure("Custom.Treeview",
                             background="#FFFFFF",
                             foreground=self.fg_color,
                             fieldbackground="#FFFFFF",
                             rowheight=25,
                             font=("Helvetica", 10))
        self.style.map("Custom.Treeview",
                       background=[('selected', self.accent_color)],
                       foreground=[('selected', '#FFFFFF')])
        
        self.style.configure("Custom.Treeview.Heading",
                             background=self.accent_color,
                             foreground="#FFFFFF",
                             font=("Helvetica", 10, "bold"))

    def create_widgets(self):
        self.main_frame = ttk.Frame(self.root, style="Custom.TFrame")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        title_label = ttk.Label(self.main_frame, text="🚨 ResQnect: Disaster Response and Relief Management System 🚨", style="Custom.TLabel")
        title_label.pack(pady=(0, 20))

        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.notebook.add(self.create_volunteer_tab(), text="Manage Volunteers")
        self.notebook.add(self.create_resource_tab(), text="Manage Resources")
        self.notebook.add(self.create_task_tab(), text="Assign Tasks")
        self.notebook.add(self.create_disaster_tab(), text="Track Disasters")
        self.notebook.add(self.create_response_time_report_tab(), text="Response Time Reports")

        exit_btn = ttk.Button(self.main_frame, text="Exit", style="Custom.TButton", command=self.exit_application)
        exit_btn.pack(pady=10)

    def create_volunteer_tab(self):
        frame = ttk.Frame(self.notebook, style="Custom.TFrame")

        ttk.Label(frame, text="Add New Volunteer", style="Custom.TLabel").pack(anchor="w", pady=(0, 10))
        self.volunteer_name_entry = ttk.Entry(frame, width=50)
        self.volunteer_name_entry.pack(fill=tk.X, pady=(0, 10))
        ttk.Label(frame, text="Volunteer Type:", style="Custom.TLabel").pack(anchor="w")
        self.volunteer_type_entry = ttk.Entry(frame, width=50)
        self.volunteer_type_entry.pack(fill=tk.X, pady=(0, 10))
        ttk.Label(frame, text="Availability (Yes/No):", style="Custom.TLabel").pack(anchor="w")
        self.volunteer_availability_entry = ttk.Entry(frame, width=50)
        self.volunteer_availability_entry.pack(fill=tk.X, pady=(0, 10))

        add_volunteer_btn = ttk.Button(frame, text="Add Volunteer", style="Custom.TButton", command=self.add_volunteer)
        add_volunteer_btn.pack(pady=(10, 20))

        self.volunteer_tree = ttk.Treeview(frame, columns=("Name", "Type", "Availability"), show="headings", style="Custom.Treeview")
        self.volunteer_tree.heading("Name", text="Name")
        self.volunteer_tree.heading("Type", text="Volunteer Type")
        self.volunteer_tree.heading("Availability", text="Availability")
        self.volunteer_tree.column("Name", anchor="w", width=200)
        self.volunteer_tree.column("Type", anchor="w", width=150)
        self.volunteer_tree.column("Availability", anchor="w", width=100)
        self.volunteer_tree.pack(fill=tk.BOTH, expand=True, pady=10)

        self.volunteer_tree.tag_configure("row", background="#FFFFFF")
        self.volunteer_tree.tag_configure("altrow", background="#F0F0F0")

        refresh_btn = ttk.Button(frame, text="Refresh List", style="Custom.TButton", command=self.refresh_volunteers)
        refresh_btn.pack(pady=10)

        return frame

    def create_resource_tab(self):
        frame = ttk.Frame(self.notebook, style="Custom.TFrame")

        ttk.Label(frame, text="Add New Resource", style="Custom.TLabel").pack(anchor="w", pady=(0, 10))
        self.resource_name_entry = ttk.Entry(frame, width=50)
        self.resource_name_entry.pack(fill=tk.X, pady=(0, 10))
        ttk.Label(frame, text="Quantity:", style="Custom.TLabel").pack(anchor="w")
        self.resource_quantity_entry = ttk.Entry(frame, width=50)
        self.resource_quantity_entry.pack(fill=tk.X, pady=(0, 10))
        ttk.Label(frame, text="Is it Monetary? (Yes/No):", style="Custom.TLabel").pack(anchor="w")
        self.resource_monetary_entry = ttk.Entry(frame, width=50)
        self.resource_monetary_entry.pack(fill=tk.X, pady=(0, 10))

        add_resource_btn = ttk.Button(frame, text="Add Resource", style="Custom.TButton", command=self.add_resource)
        add_resource_btn.pack(pady=(10, 20))

        self.resource_tree = ttk.Treeview(frame, columns=("Resource Type", "Quantity", "Monetary"), show="headings", style="Custom.Treeview")
        self.resource_tree.heading("Resource Type", text="Resource Type")
        self.resource_tree.heading("Quantity", text="Quantity")
        self.resource_tree.heading("Monetary", text="Monetary?")
        self.resource_tree.column("Resource Type", anchor="w", width=200)
        self.resource_tree.column("Quantity", anchor="w", width=150)
        self.resource_tree.column("Monetary", anchor="w", width=100)
        self.resource_tree.pack(fill=tk.BOTH, expand=True, pady=10)

        self.resource_tree.tag_configure("row", background="#FFFFFF")
        self.resource_tree.tag_configure("altrow", background="#F0F0F0")

        refresh_btn = ttk.Button(frame, text="Refresh List", style="Custom.TButton", command=self.refresh_resources)
        refresh_btn.pack(pady=10)

        return frame

    def create_task_tab(self):
        frame = ttk.Frame(self.notebook, style="Custom.TFrame")

        ttk.Label(frame, text="Assign Task", style="Custom.TLabel").pack(anchor="w", pady=(0, 10))
        ttk.Label(frame, text="Task Description:", style="Custom.TLabel").pack(anchor="w")
        self.task_description_entry = ttk.Entry(frame, width=50)
        self.task_description_entry.pack(fill=tk.X, pady=(0, 10))
        ttk.Label(frame, text="Volunteer Name:", style="Custom.TLabel").pack(anchor="w")
        self.task_volunteer_name_entry = ttk.Entry(frame, width=50)
        self.task_volunteer_name_entry.pack(fill=tk.X, pady=(0, 10))

        assign_task_btn = ttk.Button(frame, text="Assign Task", style="Custom.TButton", command=self.assign_task)
        assign_task_btn.pack(pady=(10, 20))

        return frame

    def create_disaster_tab(self):
        frame = ttk.Frame(self.notebook, style="Custom.TFrame")

        ttk.Label(frame, text="Track Disaster Response", style="Custom.TLabel").pack(anchor="w", pady=(0, 10))

        self.disaster_response_tree = ttk.Treeview(frame, columns=("Status", "Volunteer Name", "Task Assigned"), show="headings", style="Custom.Treeview")
        self.disaster_response_tree.heading("Status", text="Status")
        self.disaster_response_tree.heading("Volunteer Name", text="Volunteer Name")
        self.disaster_response_tree.heading("Task Assigned", text="Task Assigned")
        self.disaster_response_tree.column("Status", anchor="w", width=150)
        self.disaster_response_tree.column("Volunteer Name", anchor="w", width=200)
        self.disaster_response_tree.column("Task Assigned", anchor="w", width=200)
        self.disaster_response_tree.pack(fill=tk.BOTH, expand=True, pady=10)

        self.disaster_response_tree.tag_configure("row", background="#FFFFFF")
        self.disaster_response_tree.tag_configure("altrow", background="#F0F0F0")

        refresh_btn = ttk.Button(frame, text="Refresh", style="Custom.TButton", command=self.refresh_disaster_response)
        refresh_btn.pack(pady=10)

        return frame

    def create_response_time_report_tab(self):
        frame = ttk.Frame(self.notebook, style="Custom.TFrame")

        ttk.Label(frame, text="Response Time Reports", style="Custom.TLabel").pack(anchor="w", pady=(0, 10))

        self.response_time_tree = ttk.Treeview(frame, columns=("Task", "Assigned Time", "Completion Time", "Time Taken"), show="headings", style="Custom.Treeview")
        self.response_time_tree.heading("Task", text="Task Description")
        self.response_time_tree.heading("Assigned Time", text="Assigned Time")
        self.response_time_tree.heading("Completion Time", text="Completion Time")
        self.response_time_tree.heading("Time Taken", text="Time Taken")
        self.response_time_tree.column("Task", anchor="w", width=200)
        self.response_time_tree.column("Assigned Time", anchor="w", width=150)
        self.response_time_tree.column("Completion Time", anchor="w", width=150)
        self.response_time_tree.column("Time Taken", anchor="w", width=150)
        self.response_time_tree.pack(fill=tk.BOTH, expand=True, pady=10)

        self.response_time_tree.tag_configure("row", background="#FFFFFF")
        self.response_time_tree.tag_configure("altrow", background="#F0F0F0")

        return frame

    def add_volunteer(self):
        name = self.volunteer_name_entry.get()
        type_ = self.volunteer_type_entry.get()
        availability = self.volunteer_availability_entry.get()

        try:
        # Check if name, type, and availability are valid (non-numeric)
            if not name.isalpha():
                raise ValueError("Name should not contain numbers.")
            if not type_.isalpha():
                raise ValueError("Volunteer type should not contain numbers.")
            if not availability.isalpha():
                raise ValueError("Availability should only be 'Yes' or 'No'.")

            if name and type_ and availability:
                volunteer = {"name": name, "type": type_, "availability": availability}
                self.system.add_volunteer(volunteer)  # Add the volunteer to the system
                self.refresh_volunteers()
                messagebox.showinfo("Success", "Volunteer added successfully!")
            else:
                messagebox.showerror("Error", "All fields must be filled out.")

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
        
    def refresh_volunteers(self):
        self.volunteer_tree.delete(*self.volunteer_tree.get_children())
        for volunteer in self.system.volunteers:
            self.volunteer_tree.insert("", tk.END, values=(volunteer["name"], volunteer["type"], volunteer["availability"]))

    def add_resource(self):
        name = self.resource_name_entry.get()
        quantity = self.resource_quantity_entry.get()
        monetary = self.resource_monetary_entry.get()

        try:
        # Check if quantity is a number
            if not quantity.isdigit():
                raise ValueError("Quantity should be a valid number.")
        # Validate that name and monetary don't contain numeric characters
            if any(char.isdigit() for char in name):
                raise ValueError("Resource name should not contain numbers.")
            if not monetary.isalpha():
                raise ValueError("Monetary should be 'Yes' or 'No'.")

            if name and quantity and monetary:
                resource = {"name": name, "quantity": quantity, "monetary": monetary}
                self.system.add_resource(resource)
                self.refresh_resources()
                messagebox.showinfo("Success", "Resource added successfully!")
            else:
                messagebox.showerror("Error", "All fields must be filled out.")

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def refresh_resources(self):
        self.resource_tree.delete(*self.resource_tree.get_children())
        for resource in self.system.resources:
            self.resource_tree.insert("", tk.END, values=(resource["name"], resource["quantity"], resource["monetary"]))

    def assign_task(self):
        task_description = self.task_description_entry.get()
        volunteer_name = self.task_volunteer_name_entry.get()

        if task_description and volunteer_name:
            task = {"description": task_description, "volunteer": volunteer_name}
            self.system.assign_task(task)
            messagebox.showinfo("Success", "Task assigned successfully!")
        else:
            messagebox.showerror("Error", "All fields must be filled out.")

    def refresh_disaster_response(self):
        self.disaster_response_tree.delete(*self.disaster_response_tree.get_children())
        for disaster in self.system.disasters:
            self.disaster_response_tree.insert("", tk.END, values=(disaster["status"], disaster["volunteer"], disaster["task_assigned"]))

    def exit_application(self):
        messagebox.showinfo("Exit", "🚨 Prepare, Respond, Recover, Repeat! 🚨")
        self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    ui = DisasterResponseUI()
    ui.run()
