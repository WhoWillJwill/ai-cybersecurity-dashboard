import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

PG_DB       = os.getenv("PG_DB")
PG_USER     = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_HOST     = os.getenv("PG_HOST", "localhost")
PG_PORT     = os.getenv("PG_PORT", "5432")


def create_connection():
    """Create a connection to PostgreSQL."""
    return psycopg2.connect(
        dbname=PG_DB,
        user=PG_USER,
        password=PG_PASSWORD,
        host=PG_HOST,
        port=PG_PORT
    )


def create_table(conn):
    """Create the security_logs table if it doesn't exist."""
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS security_logs (
        id SERIAL PRIMARY KEY,
        timestamp TEXT,
        source_ip TEXT,
        event_type TEXT,
        severity TEXT,
        description TEXT
    )
    """)
    conn.commit()


def main():
    conn = create_connection()
    create_table(conn)
    conn.close()
    print("PostgreSQL database table created successfully.")


if __name__ == "__main__":
    main()
