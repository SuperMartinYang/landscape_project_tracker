import tkinter as tk
from tkinter import ttk, messagebox
import database
from project_list import ProjectListFrame  # Ensure to import ProjectListFrame

class CreateProjectFrame(ttk.LabelFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, text="Create Project")
        self.controller = controller
        self.setup_frame()

    def setup_frame(self):
        ttk.Label(self, text="Address:").grid(row=0, column=0, padx=5, pady=5)
        self.address_entry = ttk.Entry(self, width=30)
        self.address_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="Owner:").grid(row=1, column=0, padx=5, pady=5)
        self.owner_entry = ttk.Entry(self, width=30)
        self.owner_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text="Phone:").grid(row=2, column=0, padx=5, pady=5)
        self.phone_entry = ttk.Entry(self, width=30)
        self.phone_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self, text="Total Price ($):").grid(row=3, column=0, padx=5, pady=5)
        self.total_price_entry = ttk.Entry(self, width=10)
        self.total_price_entry.grid(row=3, column=1, padx=5, pady=5)

        self.create_button = ttk.Button(self, text="Create Project", command=self.create_project)
        self.create_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def create_project(self):
        address = self.address_entry.get()
        owner = self.owner_entry.get()
        phone = self.phone_entry.get()
        total_price = self.total_price_entry.get()
        status = "Quote"

        if not address or not owner or not phone or not total_price:
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            total_price = float(total_price)
        except ValueError:
            messagebox.showerror("Error", "Total price must be a number")
            return

        query = "INSERT INTO projects (address, owner, phone, status, total_price) VALUES (?, ?, ?, ?, ?)"
        parameters = (address, owner, phone, status, total_price)
        project_id = database.execute_query(query, parameters)

        print(project_id)

        messagebox.showinfo("Success", "Project created successfully")
        self.clear_fields()
        self.controller.load_projects()
        self.controller.frames["ProjectListFrame"].select_project(project_id)

    def clear_fields(self):
        self.address_entry.delete(0, tk.END)
        self.owner_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.total_price_entry.delete(0, tk.END)
