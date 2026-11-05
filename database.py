import sqlite3
conn = sqlite3.connect("home.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS devices(
id INTEGER PRIMARY KEY AUTOINCREMENT,
light1 TEXT,
light2 TEXT
)
""")

# Insert default row
conn.execute("INSERT INTO devices (light1, light2) VALUES ('off','off')")
conn.commit()
conn.close()