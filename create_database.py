import sqlite3
from pathlib import Path

# Current project folder
BASE_DIR = Path.cwd()

print("Project Folder:", BASE_DIR)

# Create data/db folder
db_folder = BASE_DIR / "data" / "db"
db_folder.mkdir(parents=True, exist_ok=True)

# Database path
db_path = db_folder / "bluestock_mf.db"

# Create database
conn = sqlite3.connect(db_path)
conn.close()

print("✅ Database created at:")
print(db_path)