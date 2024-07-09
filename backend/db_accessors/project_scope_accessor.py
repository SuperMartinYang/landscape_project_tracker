import sqlite3
from models.project_scope import ProjectScope

class ProjectScopeDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.create_table()

    def create_table(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS project_scope (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        project_id INTEGER NOT NULL,
                        scope TEXT NOT NULL,
                        FOREIGN KEY(project_id) REFERENCES projects(id))''')
        self.conn.commit()

    def create(self, project_scope):
        c = self.conn.cursor()
        c.execute('INSERT INTO project_scope (project_id, scope) VALUES (?, ?)',
                  (project_scope.project_id, project_scope.scope))
        self.conn.commit()
        return c.lastrowid

    def read(self, scope_id):
        c = self.conn.cursor()
        c.execute('SELECT * FROM project_scope WHERE id=?', (scope_id,))
        row = c.fetchone()
        return ProjectScope(*row) if row else None

    def update(self, project_scope):
        c = self.conn.cursor()
        c.execute('''UPDATE project_scope SET project_id=?, scope=? WHERE id=?''',
                  (project_scope.project_id, project_scope.scope, project_scope.id))
        self.conn.commit()

    def delete(self, scope_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM project_scope WHERE id=?', (scope_id,))
        self.conn.commit()
