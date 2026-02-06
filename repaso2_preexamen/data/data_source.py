import os
import sqlite3

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
                    CREATE TABLE empleados(
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
                        FOREIGN KEY (empleado_id) REFERENCES empleados)
                        """)
            
            conn.commit()

            empleados = [
                ("Alejandro Gomez", "Informatica"),
                ("Antonio Lobato", "Marketing"),
                ("Jose Mendez", "Ventas"),
                ("Lucas Lucas", "Informatica"),
                ("Pepe Viyuela", "Produccion")
            ]

            cur.executemany("INSERT INTO empleados (nombre,departamento) VALUES (?,?)", empleados)

            jornadas = [
                (1, "2026-01-19", 9.0), (1, "2026-01-20", 8.5), (1, "2026-01-21", 8.0), (1, "2026-01-22", 8.5), (1, "2026-01-23", 8.5),
                (2, "2026-01-19", 8.5), (2, "2026-01-20", 7.5), (2, "2026-01-21", 8.0), (2, "2026-01-22", 8.0),
                (3, "2026-01-19", 8.0), (3, "2026-01-20", 8.0), (3, "2026-01-21", 8.0), (3, "2026-01-22", 8.0), (3, "2026-01-23", 8.0),
                (4, "2026-01-19", 10.0), (4, "2026-01-20", 9.0), (4, "2026-01-21", 8.0), (4, "2026-01-22", 8.0), (4, "2026-01-23", 7.0),
            ]

            cur.executemany("INSERT INTO jornadas (empleado_id,fecha,horas) VALUES (?,?,?)", jornadas)
            conn.commit()

    def obtener_informacion():
        with DataSource.get_connection() as conn:
            cur: sqlite3.Cursor = conn.cursor()

            cur.execute("""
                    SELECT e.nombre, e.departamento,
                        SUM(j.horas) AS total,
                        SUM(j.horas) - 40 AS exceso
                        FROM empleados e
                        JOIN jornadas j ON empleado_id = e.id
                        GROUP BY e.id
                        HAVING MAX(j.horas) > 8 AND SUM(j.horas) > 40
                        """)
            
            return[ dict(filas) for filas in cur.fetchall() ]
        
    def suma_horas(rows):
        total = len(rows)

        if rows:
            suma_horas = sum(float(filas["total"]) for filas in rows)
        else:
            suma_horas = 0

        return total, suma_horas