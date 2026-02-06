import sqlite3
import os

class DataSource:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "database.db")

    def get_connection():
        conn = sqlite3.connect(DataSource.file_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def ensure_db():
        with DataSource.get_connection() as conn:
            cur: sqlite3.Cursor = conn.cursor()

            cur.execute("DROP TABLE IF EXISTS empleados")
            cur.execute("DROP TABLE IF EXISTS jornadas")

            cur.execute("""
        CREATE TABLE empleados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            departamento TEXT NOT NULL
            )
        """)
            
            cur.execute("""
        CREATE TABLE jornadas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            empleado_id INTEGER NOT NULL,
            fecha TEXT NOT NULL,
            horas REAL NOT NULL,
            FOREIGN KEY (empleado_id) REFERENCES empleados(id)
            )
         """)
            
            conn.commit()

            empleados = [
            ("Ana López", "Administración"),
            ("Luis Pérez", "Producción"),
            ("Marta Ruiz", "Logística"),
            ("Jorge Sanz", "Producción"),
            ("Claudia Vega", "Comercial"),
            ("Pablo Navas", "Mantenimiento"),]

        cur.executemany(
        "INSERT INTO empleados(nombre, departamento) VALUES (?, ?)",
        empleados)

        jornadas = [
        (1, "2026-03-02", 9.5), (1, "2026-03-03", 7.5), (1, "2026-03-04", 7.5), (1, "2026-03-05", 7.5), (1, "2026-03-06", 7.0),
        (2, "2026-03-02", 9.2), (2, "2026-03-03", 7.0), (2, "2026-03-04", 7.0), (2, "2026-03-05", 6.0), (2, "2026-03-06", 7.0),
        (3, "2026-03-02", 8.0), (3, "2026-03-03", 8.0), (3, "2026-03-04", 7.5), (3, "2026-03-05", 7.5), (3, "2026-03-06", 7.0),
        (4, "2026-03-02",10.0), (4, "2026-03-03", 8.0), (4, "2026-03-04", 8.0), (4, "2026-03-05", 8.0), (4, "2026-03-06", 7.0),
        (5, "2026-03-02", 9.1), (5, "2026-03-03", 7.6), (5, "2026-03-04", 7.6), (5, "2026-03-05", 6.8), (5, "2026-03-06", 6.5),
        (6, "2026-03-02",11.0), (6, "2026-03-03", 7.0), (6, "2026-03-04", 7.0), (6, "2026-03-05", 6.5), (6, "2026-03-06", 6.0),
        ]

        cur.executemany(
        "INSERT INTO jornadas(empleado_id, fecha, horas) VALUES (?, ?, ?)",
        jornadas)

        conn.commit()
    
    def obtener_informacion():
        with DataSource.get_connection() as conn:
            cur: sqlite3.Cursor = conn.cursor()

            cur.execute("""SELECT
e.nombre,
e.departamento,
j.fecha,
j.horas
FROM empleados e
JOIN jornadas j ON j.empleado_id = e.id
ORDER BY e.nombre ASC, j.fecha ASC;""")
            
        return[ dict(filas) for filas in cur.fetchall() ]
 