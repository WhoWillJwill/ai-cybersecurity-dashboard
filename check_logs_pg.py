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


def fetch_all_logs(conn):
    """Fetch all logs ordered by most recent timestamp."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM security_logs ORDER BY timestamp DESC")
    return cursor.fetchall()


def display_logs(logs):
    """Print all security logs in a readable format."""
    if not logs:
        print("No logs found.")
        return

    print("\n=== All Security Logs ===")
    for log in logs:
        print(f"ID: {log[0]}, Time: {log[1]}, IP: {log[2]}, "
              f"Event: {log[3]}, Severity: {log[4]}, Desc: {log[5]}")


def main():
    conn = create_connection()
    logs = fetch_all_logs(conn)
    display_logs(logs)
    conn.close()


if __name__ == "__main__":
    main()
