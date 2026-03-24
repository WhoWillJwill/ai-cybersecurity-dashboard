import sqlite3
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

SQLITE_DB   = "security.db"

PG_DB       = os.getenv("PG_DB")
PG_USER     = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_HOST     = os.getenv("PG_HOST", "localhost")
PG_PORT     = os.getenv("PG_PORT", "5432")

# --- Step 1: Connect to SQLite ---
sqlite_conn = sqlite3.connect(SQLITE_DB)
sqlite_cursor = sqlite_conn.cursor()

sqlite_cursor.execute("SELECT timestamp, source_ip, event_type, severity, description FROM security_logs")
logs = sqlite_cursor.fetchall()

print(f"Fetched {len(logs)} rows from SQLite.")

# --- Step 2: Connect to PostgreSQL ---
pg_conn = psycopg2.connect(
    dbname=PG_DB,
    user=PG_USER,
    password=PG_PASSWORD,
    host=PG_HOST,
    port=PG_PORT
)
pg_cursor = pg_conn.cursor()

# --- Step 3: Create table in Postgres if it doesn't exist ---
create_table_query = """
CREATE TABLE IF NOT EXISTS security_logs (
    id SERIAL PRIMARY KEY,
    timestamp TEXT,
    source_ip TEXT,
    event_type TEXT,
    severity TEXT,
    description TEXT
)
"""
pg_cursor.execute(create_table_query)
pg_conn.commit()
print("Postgres table ready.")

# --- Step 4: Insert logs into Postgres ---
insert_query = """
INSERT INTO security_logs (timestamp, source_ip, event_type, severity, description)
VALUES (%s, %s, %s, %s, %s)
"""

for log in logs:
    pg_cursor.execute(insert_query, log)

pg_conn.commit()
print(f"Inserted {len(logs)} rows into Postgres.")

# --- Step 5: Close connections ---
sqlite_conn.close()
pg_conn.close()
print("Migration complete!")
