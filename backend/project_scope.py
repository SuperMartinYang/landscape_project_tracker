import tkinter as tk
from tkinter import ttk, messagebox
import database

class ProjectScopeFrame(ttk.LabelFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, text="Project Scope")
        self.controller = controller
        self.setup_frame()

    def setup_frame(self):
        ttk.Label(self, text="Project ID:").grid(row=0, column=0, padx=5, pady=5)
        self.scope_project_id_entry = ttk.Entry(self, width=10)
        self.scope_project_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="Scope:").grid(row=1, column=0, padx=5, pady=5)
        self.scope_entry = ttk.Entry(self, width=30)
        self.scope_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_scope_button = ttk.Button(self, text="Add Scope", command=self.add_scope)
        self.add_scope_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def add_scope(self):
        project_id = self.scope_project_id_entry.get()
        scope = self.scope_entry.get()

        if not project_id or not scope:
            messagebox.showerror("Error", "All fields are required")
            return

        database.execute_query("INSERT INTO project_scope (project_id, scope) VALUES (?, ?)", (project_id, scope))

        messagebox.showinfo("Success", "Scope added successfully")
        self.clear_fields()
        self.controller.frames["ProjectListFrame"].select_project(project_id)

    def clear_fields(self):
        self.scope_entry.delete(0, tk.END)
