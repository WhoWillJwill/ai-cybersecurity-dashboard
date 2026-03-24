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


def fetch_high_severity_threats(conn):
    """Fetch all logs with High severity."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM security_logs WHERE severity=%s", ("High",))
    return cursor.fetchall()


def display_threats(threats, title="Threats"):
    """Print threats in a readable format."""
    if not threats:
        print(f"No {title.lower()} found.")
        return

    print(f"\n=== {title} ===")
    for threat in threats:
        print(f"ID: {threat[0]}, Time: {threat[1]}, IP: {threat[2]}, "
              f"Event: {threat[3]}, Severity: {threat[4]}, Desc: {threat[5]}")


def main():
    conn = create_connection()
    high_threats = fetch_high_severity_threats(conn)
    display_threats(high_threats, "High-Severity Threats")
    conn.close()


if __name__ == "__main__":
    main()
