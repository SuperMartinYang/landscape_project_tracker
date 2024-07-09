import sqlite3
from models.project_progress import ProjectProgress 

class ProjectProgressDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.create_table()

    def create_table(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS project_progress (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        project_id INTEGER NOT NULL,
                        work_done TEXT NOT NULL,
                        payment_percentage REAL NOT NULL,
                        payment_value REAL NOT NULL,
                        FOREIGN KEY(project_id) REFERENCES projects(id))''')
        self.conn.commit()

    def create(self, project_progress):
        c = self.conn.cursor()
        c.execute('INSERT INTO project_progress (project_id, work_done, payment_percentage, payment_value) VALUES (?, ?, ?, ?)',
                  (project_progress.project_id, project_progress.work_done, project_progress.payment_percentage, project_progress.payment_value))
        self.conn.commit()
        return c.lastrowid

    def read(self, progress_id):
        c = self.conn.cursor()
        c.execute('SELECT * FROM project_progress WHERE id=?', (progress_id,))
        row = c.fetchone()
        return ProjectProgress(*row) if row else None

    def update(self, project_progress):
        c = self.conn.cursor()
        c.execute('''UPDATE project_progress SET project_id=?, work_done=?, payment_percentage=?, payment_value=? WHERE id=?''',
                  (project_progress.project_id, project_progress.work_done, project_progress.payment_percentage, project_progress.payment_value, project_progress.id))
        self.conn.commit()

    def delete(self, progress_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM project_progress WHERE id=?', (progress_id,))
        self.conn.commit()