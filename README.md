# 🛡️ Security Dashboard

A Python-powered security log monitoring system with a PostgreSQL backend and Power BI visualization layer. Simulates, stores, and analyzes network security events — including threat detection, severity filtering, and full audit logging.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Scripts](#scripts)
- [Power BI Dashboard](#power-bi-dashboard)
- [Database Schema](#database-schema)
- [Environment Variables](#environment-variables)

---

## Overview

This project provides a lightweight security operations pipeline:

1. **Generate** simulated security logs (failed logins, malware detections, port scans, unauthorized access)
2. **Store** them in a PostgreSQL database with severity levels and timestamps
3. **Query** logs and surface high-severity threats
4. **Visualize** trends and patterns in a Power BI dashboard
5. **Migrate** data from an existing SQLite database if needed

---

## Project Structure

```
security-dashboard/
│
├── scripts/
│   ├── create_db_pg.py         # Initialize the PostgreSQL table
│   ├── log_generator_pg.py     # Generate randomized security log entries
│   ├── ai_detector_pg.py       # Surface and display high-severity threats
│   ├── check_logs_pg.py        # View all logs ordered by timestamp
│   └── sqlite_to_postgres.py   # Migrate existing SQLite data to PostgreSQL
│
├── dashboard/
│   └── cc.pbix                 # Power BI dashboard file
│
├── .env.example                # Template for environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Tech Stack

| Layer        | Technology              |
|--------------|-------------------------|
| Language     | Python 3.x              |
| Database     | PostgreSQL              |
| DB Driver    | psycopg2                |
| Visualization| Power BI Desktop        |
| Migration    | SQLite → PostgreSQL     |

---

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL installed and running
- Power BI Desktop (for the dashboard)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/security-dashboard.git
cd security-dashboard
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Configure environment variables**

```bash
cp .env.example .env
```

Open `.env` and fill in your PostgreSQL credentials (see [Environment Variables](#environment-variables)).

**4. Create the database table**

```bash
python scripts/create_db_pg.py
```

**5. Generate sample logs**

```bash
python scripts/log_generator_pg.py
```

You're ready to go.

---

## Scripts

### `create_db_pg.py`
Initializes the `security_logs` table in your PostgreSQL database. Safe to re-run — uses `CREATE TABLE IF NOT EXISTS`.

```bash
python scripts/create_db_pg.py
```

---

### `log_generator_pg.py`
Inserts 50 randomized security log entries into the database. Each entry includes a timestamp, a random source IP, an event type, and a severity level.

```bash
python scripts/log_generator_pg.py
```

Event types: `Failed Login`, `Malware Detected`, `Port Scan`, `Unauthorized Access`  
Severity levels: `Low`, `Medium`, `High`

---

### `ai_detector_pg.py`
Fetches and displays all `High` severity entries from the logs table — simulating an automated threat detection layer.

```bash
python scripts/ai_detector_pg.py
```

---

### `check_logs_pg.py`
Displays all security logs ordered by most recent timestamp.

```bash
python scripts/check_logs_pg.py
```

---

### `sqlite_to_postgres.py`
One-time migration script. Reads all rows from a local `security.db` SQLite file and inserts them into PostgreSQL. Creates the destination table if it doesn't exist.

```bash
python scripts/sqlite_to_postgres.py
```

> **Note:** Place your `security.db` file in the project root before running.

---

## Power BI Dashboard

The `dashboard/cc.pbix` file connects to your PostgreSQL database and visualizes:

- Log volume over time
- Event type breakdown
- Severity distribution
- Source IP activity

To use it, open the file in **Power BI Desktop** and update the data source connection to point to your local PostgreSQL instance.

---

## Database Schema

**Table: `security_logs`**

| Column       | Type    | Description                        |
|--------------|---------|------------------------------------|
| `id`         | SERIAL  | Auto-incrementing primary key      |
| `timestamp`  | TEXT    | Date and time of the event         |
| `source_ip`  | TEXT    | Source IP address                  |
| `event_type` | TEXT    | Type of security event             |
| `severity`   | TEXT    | Severity level (Low, Medium, High) |
| `description`| TEXT    | Human-readable description         |

---

## Environment Variables

This project uses a `.env` file to keep credentials out of source code. **Never commit your `.env` file.**

Copy `.env.example` to `.env` and fill in your values:

```
PG_DB=security_Dashboard
PG_USER=your_postgres_username
PG_PASSWORD=your_postgres_password
PG_HOST=localhost
PG_PORT=5432
```

---

## ⚠️ Security Note

Ensure your `.env` file is listed in `.gitignore` before pushing to GitHub. Database credentials should never be committed to version control.

---

## License

MIT License — feel free to use, modify, and distribute.
