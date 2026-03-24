import psycopg2
import random
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

PG_DB       = os.getenv("PG_DB")
PG_USER     = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_HOST     = os.getenv("PG_HOST", "localhost")
PG_PORT     = os.getenv("PG_PORT", "5432")

EVENTS     = ["Failed Login", "Malware Detected", "Port Scan", "Unauthorized Access"]
SEVERITIES = ["Low", "Medium", "High"]


def create_connection():
    """Create a connection to PostgreSQL."""
    return psycopg2.connect(
        dbname=PG_DB,
        user=PG_USER,
        password=PG_PASSWORD,
        host=PG_HOST,
        port=PG_PORT
    )


def generate_random_ip():
    """Generate a random IPv4 address."""
    return f"192.168.1.{random.randint(1, 255)}"


def insert_log(conn, event_type, severity, description="Suspicious activity detected"):
    """Insert a single security log into PostgreSQL."""
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO security_logs (timestamp, source_ip, event_type, severity, description)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        generate_random_ip(),
        event_type,
        severity,
        description
    ))
    conn.commit()


def generate_logs(conn, num_logs=50):
    """Generate multiple random security logs."""
    for _ in range(num_logs):
        insert_log(conn, random.choice(EVENTS), random.choice(SEVERITIES))


def main():
    conn = create_connection()
    generate_logs(conn)
    conn.close()
    print("Security logs generated successfully in PostgreSQL.")


if __name__ == "__main__":
    main()
