import sqlite3

def setup_database():
    conn = sqlite3.connect('landscape_project_tracker.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    address TEXT NOT NULL,
                    owner TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    status TEXT,
                    total_price REAL NOT NULL DEFAULT 0)''')
    c.execute('''CREATE TABLE IF NOT EXISTS project_scope (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id INTEGER NOT NULL,
                    scope TEXT NOT NULL,
                    FOREIGN KEY(project_id) REFERENCES projects(id))''')
    c.execute('''CREATE TABLE IF NOT EXISTS project_progress (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id INTEGER NOT NULL,
                    work_done TEXT NOT NULL,
                    payment_percentage REAL NOT NULL,
                    payment_value REAL NOT NULL,
                    FOREIGN KEY(project_id) REFERENCES projects(id))''')
    conn.commit()
    conn.close()

def execute_query(query, parameters=()):
    conn = sqlite3.connect('landscape_project_tracker.db')
    c = conn.cursor()
    c.execute(query, parameters)
    lastId = c.lastrowid
    conn.commit()
    conn.close()
    return lastId

def fetch_query(query, params=()):
    conn = sqlite3.connect('landscape_project_tracker.db')
    c = conn.cursor()
    c.execute(query, params)
    results = c.fetchall()
    conn.close()
    return results
