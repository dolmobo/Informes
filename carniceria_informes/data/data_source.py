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
                CREATE TABLE IF NOT EXISTS carniceria (
                        carne TEXT NOT NULL,
                        tipo TEXT NOT NULL,
                        peso INTEGER NOT NULL
                        )
                """)
            
            conn.commit()

            cur.execute("SELECT COUNT (*) FROM carniceria")
            count = cur.fetchone()[0]

            if count == 0:

                datos = [
                    ("Pollo", "Blanca", 23),
                    ("Cerdo", "Roja", 43),
                    ("Ternera", "Roja", 45),
                    ("Res", "Roja", 54)
                ]

                cur.executemany("INSERT INTO carniceria VALUES (?,?,?)", datos)
                conn.commit()

    def obtener_carnes():
        with DataSource.get_connection() as conn:
            cur: sqlite3.Cursor = conn.cursor()

            cur.execute("SELECT * FROM carniceria ORDER BY carne")
            
            return[ dict(filas) for filas in cur.fetchall() ]
        
    def suma_kg(rows):
        total = len(rows)

        if rows:
            suma_kg = sum(int (fila["peso"]) for fila in rows)
        else:
            suma_kg = 0

        return total,suma_kg