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
            cur: sqlite3.Cursor = conn.cursor()

            cur.execute("""
            CREATE TABLE IF NOT EXISTS ferreteria (
                        repuesto TEXT NOT NULL,
                        descripcion TEXT NOT NULL,
                        precio INTEGER NOT NULL
                        )
            """)

            conn.commit()

            cur.execute("SELECT COUNT (*) FROM ferreteria")
            count = cur.fetchone()[0]

            if count == 0:
                datos = [
                    ("Bombilla", "Bombilla LED, bajo consumo", 3),
                    ("Copia llave", "Copia de llave", 1),
                    ("Repuestos para cortadora", "Repuestos para cortadora de hierba", 2)
                ]

                cur.executemany("INSERT INTO ferreteria VALUES (?,?,?)", datos)
                conn.commit()

    def obtener_repuestos():
        with DataSource.get_connection() as conn:
            cur: sqlite3.Cursor = conn.cursor()

            cur.execute("SELECT * FROM ferreteria ORDER BY repuesto, descripcion")

            return [ dict(filas) for filas in cur.fetchall() ]
        
    def suma_precio(rows):
        total = len(rows)
        if rows:
            suma_precio = sum(int (r["precio"]) for r in rows)
        else:
            suma_precio = 0

        return total, suma_precio