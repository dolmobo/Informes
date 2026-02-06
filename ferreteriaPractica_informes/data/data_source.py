import os
import sqlite3

class DataSource:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "control_horario.db") 

    def get_connection():
        conn = sqlite3.connect(DataSource.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def ensure_db():
        with DataSource.get_connection() as conn:
            cur = conn.cursor()

            # Tablas nuevas
            cur.execute("DROP TABLE IF EXISTS jornadas")
            cur.execute("DROP TABLE IF EXISTS empleados")

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

            # Datos de prueba
            empleados = [
                ("Ana López", "Administración"),
                ("Luis Pérez", "Producción"),
                ("Marta Ruiz", "Logística"),
                ("Jorge Sanz", "Producción"),
            ]
            cur.executemany("INSERT INTO empleados(nombre, departamento) VALUES (?, ?)", empleados)

            jornadas = [
                (1, "2026-01-19", 9.0), (1, "2026-01-20", 8.5), (1, "2026-01-21", 8.0), (1, "2026-01-22", 8.5), (1, "2026-01-23", 8.5),
                (2, "2026-01-19", 8.5), (2, "2026-01-20", 7.5), (2, "2026-01-21", 8.0), (2, "2026-01-22", 8.0),
                (3, "2026-01-19", 8.0), (3, "2026-01-20", 8.0), (3, "2026-01-21", 8.0), (3, "2026-01-22", 8.0), (3, "2026-01-23", 8.0),
                (4, "2026-01-19", 10.0), (4, "2026-01-20", 9.0), (4, "2026-01-21", 8.0), (4, "2026-01-22", 8.0), (4, "2026-01-23", 7.0),
            ]
            cur.executemany("INSERT INTO jornadas(empleado_id, fecha, horas) VALUES (?, ?, ?)", jornadas)
            conn.commit()

    def obtener_informe_horas():
        with DataSource.get_connection() as conn:
            cur = conn.cursor()
            # Esta es la query clave del examen:
            cur.execute("""
                SELECT
                    e.nombre,
                    e.departamento,
                    SUM(j.horas) AS total,
                    SUM(j.horas) - 40 AS exceso
                FROM empleados e
                JOIN jornadas j ON j.empleado_id = e.id
                GROUP BY e.id
                HAVING MAX(j.horas) > 8 AND SUM(j.horas) > 40
            """)
            return [dict(row) for row in cur.fetchall()]