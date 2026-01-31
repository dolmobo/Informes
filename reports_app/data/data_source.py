import os
import sqlite3
from typing import List, Dict, Tuple

def get_db_path(base_dir: str) -> str:
    return os.path.join(base_dir, "data", "database.db")

def ensure_db(db_path: str) -> None:
    """Create the SQLite DB + table if missing, and insert sample data if empty."""
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS participants (
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                points INTEGER NOT NULL
            )
            """
        )
        conn.commit()

        cur.execute("SELECT COUNT(*) FROM participants")
        (count,) = cur.fetchone()
        if count == 0:
            sample = [
                ("Ana García", "Ventas", 120),
                ("Carlos Pérez", "Ventas", 95),
                ("Lucía Martín", "Marketing", 110),
                ("Sofía López", "Marketing", 70),
                ("Diego Sánchez", "IT", 150),
                ("María Torres", "IT", 130),
                ("Javier Ruiz", "RRHH", 80),
                ("Paula Romero", "RRHH", 90),
                ("Hugo Navarro", "Finanzas", 140),
            ]
            cur.executemany(
                "INSERT INTO participants (name, department, points) VALUES (?, ?, ?)",
                sample,
            )
            conn.commit()

def fetch_participants(db_path: str) -> List[Dict]:
    """Read participants ordered by department (ampliación) and name."""
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(
            """
            SELECT name, department, points
            FROM participants
            ORDER BY department COLLATE NOCASE ASC, name COLLATE NOCASE ASC
            """
        )
        return [dict(r) for r in cur.fetchall()]

def compute_summary(rows: List[Dict]) -> Tuple[int, int]:
    total = len(rows)
    points_sum = sum(int(r["points"]) for r in rows) if rows else 0
    return total, points_sum
