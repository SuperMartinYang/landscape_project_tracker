import tkinter as tk
from tkinter import ttk, messagebox
from create_project import CreateProjectFrame
from project_scope import ProjectScopeFrame
from track_project import TrackProjectFrame
from project_list import ProjectListFrame
import database

class LandscapeProjectTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Landscape Project Tracker")
        self.frames = {}

        self.frames["CreateProjectFrame"] = CreateProjectFrame(root, self)
        self.frames["CreateProjectFrame"].grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.frames["ProjectScopeFrame"] = ProjectScopeFrame(root, self)
        self.frames["ProjectScopeFrame"].grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.frames["TrackProjectFrame"] = TrackProjectFrame(root, self)
        self.frames["TrackProjectFrame"].grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.frames["ProjectListFrame"] = ProjectListFrame(root, self)
        self.frames["ProjectListFrame"].grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="nsew")

        self.load_projects()

    def load_projects(self):
        self.frames["ProjectListFrame"].load_projects()

if __name__ == "__main__":
    root = tk.Tk()
    database.setup_database()
    app = LandscapeProjectTracker(root)
    root.mainloop()
