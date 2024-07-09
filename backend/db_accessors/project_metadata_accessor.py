import sqlite3
from models.project_metadata import ProjectMetadata

class ProjectMetadataDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.create_table()

    def create_table(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS project_metadata (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        address TEXT NOT NULL,
                        owner TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        status TEXT,
                        total_price REAL NOT NULL DEFAULT 0)''')
        self.conn.commit()

    def create(self, project_metadata):
        c = self.conn.cursor()
        c.execute('INSERT INTO project_metadata (address, owner, phone, status, total_price) VALUES (?, ?, ?, ?, ?)',
                  (project_metadata.address, project_metadata.owner, project_metadata.phone, project_metadata.status, project_metadata.total_price))
        self.conn.commit()
        return c.lastrowid

    def read(self, project_metadata_id):
        c = self.conn.cursor()
        c.execute('SELECT * FROM project_metadata WHERE id=?', (project_metadata_id,))
        row = c.fetchone()
        return ProjectMetadata(*row) if row else None

    def update(self, project_metadata):
        c = self.conn.cursor()
        c.execute('''UPDATE project_metadata SET address=?, owner=?, phone=?, status=?, total_price=?
                     WHERE id=?''',
                  (project_metadata.address, project_metadata.owner, project_metadata.phone, project_metadata.status, project_metadata.total_price, project_metadata.id))
        self.conn.commit()

    def delete(self, project_metadata_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM project_metadata WHERE id=?', (project_metadata_id,))
        self.conn.commit()