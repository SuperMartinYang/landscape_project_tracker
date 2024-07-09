import tkinter as tk
from tkinter import ttk, messagebox
import database

class TrackProjectFrame(ttk.LabelFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, text="Track Project")
        self.controller = controller
        self.setup_frame()

    def setup_frame(self):
        ttk.Label(self, text="Project ID:").grid(row=0, column=0, padx=5, pady=5)
        self.track_project_id_entry = ttk.Entry(self, width=10)
        self.track_project_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="Work Done:").grid(row=1, column=0, padx=5, pady=5)
        self.work_done_entry = ttk.Entry(self, width=30)
        self.work_done_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text="Payment $:").grid(row=2, column=0, padx=5, pady=5)
        self.payment_value_entry = ttk.Entry(self, width=10)
        self.payment_value_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_progress_button = ttk.Button(self, text="Add Progress", command=self.add_progress)
        self.add_progress_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def add_progress(self):
        project_id = self.track_project_id_entry.get()
        work_done = self.work_done_entry.get()
        payment_value = self.payment_value_entry.get()

        if not project_id or not work_done or not payment_value:
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            payment_value = float(payment_value)
        except ValueError:
            messagebox.showerror("Error", "Payment value must be a number")
            return

        # Fetch total price from the projects table
        total_price = database.fetch_query("SELECT total_price FROM projects WHERE id=?", (project_id,))
        if not total_price:
            messagebox.showerror("Error", "Project ID not found")
            return
        total_price = total_price[0][0]

        # Calculate percentage
        if total_price > 0:
            payment_percentage = (payment_value / total_price) * 100
        else:
            payment_percentage = 0.0

        # Insert progress into project_progress table
        database.execute_query("INSERT INTO project_progress (project_id, work_done, payment_percentage, payment_value) VALUES (?, ?, ?, ?)",
                      (project_id, work_done, payment_percentage, payment_value))

        messagebox.showinfo("Success", "Progress added successfully")
        self.clear_fields()
        self.controller.load_projects()
        self.controller.frames["ProjectListFrame"].select_project(project_id)

    def clear_fields(self):
        self.work_done_entry.delete(0, tk.END)
        self.payment_value_entry.delete(0, tk.END)
