import os
import sqlite3

class DataSource:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "database.db")

    def get_connection():
        conn = sqlite3.connect(DataSource.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def ensure_db():
        with DataSource.get_connection() as conn:
            cur : sqlite3.Cursor = conn.cursor()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS manicura (
                        name TEXT NOT NULL,
                        descripcion TEXT NOT NULL,
                        precio INTEGER NOT NULL
                        )
            """)

            conn.commit()

            cur.execute("SELECT COUNT (*) FROM manicura")
            count = cur.fetchone()[0]

            if count == 0:

                datos =[
                    ("Acrygel", "Un solo color", 30),
                    ("Nivelacion", "Nivelacion semiparmanente, un solo color", 20),
                    ("Manicura acrilicas", "Un solo color", 30),
                    ("Limpieza", "Manicura en remojo con retirado de cuticulas", 8)
                ]

                cur.executemany("INSERT INTO manicura VALUES (?,?,?)", datos)
                conn.commit()

    def obtener_manicura():
        with DataSource.get_connection() as conn:
            cur: sqlite3.Cursor = conn.cursor()

            cur.execute("SELECT * FROM manicura ORDER BY name, descripcion")

            return [ dict(filas) for filas in cur.fetchall() ]
        
    def suma_precios(rows):
        total = len(rows)

        if rows:
            suma_precio = sum(int (fila["precio"]) for fila in rows)
        else:
            suma_precio = 0

        return total, suma_precio