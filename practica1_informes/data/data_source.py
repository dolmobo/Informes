import os
import sqlite3

# --- 1. RUTA DE LA BASE DE DATOS ---
def get_db_path(base_dir):
    # Une las carpetas para encontrar el archivo
    return os.path.join(base_dir, "data", "database.db")

# --- 2. PREPARACIÓN (Crear tabla y datos si hace falta) ---
def ensure_db(db_path):
    # Conectamos a la base de datos
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        
        # Crea la tabla si no existe
        cur.execute("""
            CREATE TABLE IF NOT EXISTS participants (
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                points INTEGER NOT NULL
            )
        """)
        conn.commit()

        # Si está vacía, metemos datos de prueba
        cur.execute("SELECT COUNT(*) FROM participants")
        count = cur.fetchone()[0]
        
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
            cur.executemany("INSERT INTO participants VALUES (?, ?, ?)", sample)
            conn.commit()

# --- 3. RECUPERAR DATOS (Lo que usa el informe) ---
def fetch_participants(db_path):
    with sqlite3.connect(db_path) as conn:
        # Esto es para que puedas usar nombres: fila['name']
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        
        # Pide los datos ordenados
        cur.execute("SELECT * FROM participants ORDER BY department, name")
        
        # Convierte el resultado en una lista de diccionarios normal
        return [dict(r) for r in cur.fetchall()]

# --- 4. CALCULAR TOTALES ---
def compute_summary(rows):
    total = len(rows)
    # Suma los puntos de todos
    points_sum = sum(int(r["points"]) for r in rows) if rows else 0
    
    return total, points_sum