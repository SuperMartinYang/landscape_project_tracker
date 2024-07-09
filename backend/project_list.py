import tkinter as tk
from tkinter import ttk, messagebox
import database

class ProjectListFrame(ttk.LabelFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, text="Project List")
        self.controller = controller
        self.setup_frame()

    def setup_frame(self):
        self.project_list = ttk.Treeview(self, columns=("ID", "Address", "Owner", "Phone", "Total Price"), show='headings')
        self.project_list.heading("ID", text="ID")
        self.project_list.heading("Address", text="Address")
        self.project_list.heading("Owner", text="Owner")
        self.project_list.heading("Phone", text="Phone")
        self.project_list.heading("Status", text="Status")
        self.project_list.heading("Total Price", text="Total Price ($)")
        self.project_list.bind('<<TreeviewSelect>>', self.on_project_select)
        self.project_list.pack(fill=tk.BOTH, expand=True)

        self.details_frame = ttk.Frame(self)
        
        self.details_label = ttk.Label(self.details_frame, text="Select a project to see details", anchor=tk.W)
        self.details_label.pack(fill=tk.X, padx=10, pady=5)

        # Progress Table
        self.progress_table = ttk.Treeview(self.details_frame, columns=("Work Done", "Payment Percentage", "Payment Value ($)"), show='headings')
        self.progress_table.heading("Work Done", text="Work Done")
        self.progress_table.heading("Payment Percentage", text="Payment Percentage")
        self.progress_table.heading("Payment Value ($)", text="Payment Value ($)")
        self.progress_table.pack(fill=tk.BOTH, expand=True)


        self.delete_button = ttk.Button(self, text="Delete Project", command=self.delete_project)
        self.delete_button.pack(pady=10)

        self.load_projects()  # Load projects initially

    def load_projects(self):
        self.project_list.delete(*self.project_list.get_children())

        projects = database.fetch_query("SELECT id, address, owner, phone, status, total_price FROM projects")
        for project in projects:
            self.project_list.insert("", tk.END, values=project)

    def on_project_select(self, event):
        selected_item = self.project_list.selection()
        if selected_item:
            project_id = self.project_list.item(selected_item[0])['values'][0]
            self.update_details(project_id)
            self.details_frame.pack(fill=tk.BOTH, expand=True)  # Show details frame when project is selected
            
            # show id in update panels
            self.controller.frames["ProjectScopeFrame"].scope_project_id_entry.delete(0, tk.END)
            self.controller.frames["ProjectScopeFrame"].scope_project_id_entry.insert(0, project_id)
            self.controller.frames["TrackProjectFrame"].track_project_id_entry.delete(0, tk.END)
            self.controller.frames["TrackProjectFrame"].track_project_id_entry.insert(0, project_id)
        else:
            self.clear_details()
            self.details_frame.pack_forget()  # Hide details frame if no project is selected

    def update_details(self, project_id):
        project = database.fetch_query("SELECT address, owner, phone, status, total_price FROM projects WHERE id=?", (project_id,))
        scopes = database.fetch_query("SELECT scope FROM project_scope WHERE project_id=?", (project_id,))
        progresses = database.fetch_query("SELECT work_done, payment_percentage, payment_value FROM project_progress WHERE project_id=?", (project_id,))

        details_text = f"Project ID: {project_id}\n"
        details_text += f"Address: {project[0][0]}\n"
        details_text += f"Owner: {project[0][1]}\n"
        details_text += f"Phone: {project[0][2]}\n"
        details_text += f"Status: {project[0][3]}\n"
        details_text += f"Total Price: ${project[0][4]:,.2f}\n\n"
        
        details_text += "Scopes:\n"
        for scope in scopes:
            details_text += f"- {scope[0]}\n"

        details_text += "\nProgress:\n"
        self.progress_table.delete(*self.progress_table.get_children())
        for progress in progresses:
            self.progress_table.insert("", tk.END, values=progress)

        self.details_label.config(text=details_text)

    def delete_project(self):
        selected_item = self.project_list.selection()
        if not selected_item:
            messagebox.showerror("Error", "No project selected")
            return

        confirmation = messagebox.askyesno("Confirm Deletion", "Do you really want to delete this project?")
        if confirmation:
            project_id = self.project_list.item(selected_item[0])['values'][0]

            # Delete from project_progress table
            database.execute_query("DELETE FROM project_progress WHERE project_id=?", (project_id,))

            # Delete from project_scope table
            database.execute_query("DELETE FROM project_scope WHERE project_id=?", (project_id,))

            # Delete from projects table
            database.execute_query("DELETE FROM projects WHERE id=?", (project_id,))

            messagebox.showinfo("Success", "Project deleted successfully")
            self.load_projects()  # Reload project list after deletion

    def clear_details(self):
        self.details_label.config(text="Select a project to see details")

    def select_project(self, project_id):
        for item in self.project_list.get_children():
            if self.project_list.item(item, 'values')[0] == project_id:
                self.project_list.selection_set(item)
                self.update_details(project_id)
                break

