import os
import sqlite3

class DataSource:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "fruteria.db")

    def get_connection():
        conn = sqlite3.connect(DataSource.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def const_bd():
        with DataSource.get_connection() as conn:
            cur: sqlite3.Cursor = conn.cursor()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS fruteria(
                        nombre TEXT NOT NULL,
                        tipo TEXT NOT NULL,
                        kilo INTEGER NOT NULL
                        )
            """)

            conn.commit()

            cur.execute("SELECT COUNT (*) FROM fruteria")
            count = cur.fetchone()[0]

            if count == 0:
                datos = [
                    # Lo básico
                    ("Manzana", "Fruta", 20),
                    ("Pera", "Fruta", 15),
                    
                    # Cítricos
                    ("Limón", "Cítrico", 10),
                    ("Naranja", "Cítrico", 25),
                    ("Mandarina", "Cítrico", 18),
                    ("Pomelo", "Cítrico", 5),
                    
                    # Frutas normales
                    ("Plátano", "Fruta", 30),
                    ("Uva", "Fruta", 12),
                    ("Fresa", "Fruta", 8),
                    
                    ("Mango", "Tropical", 10),
                    ("Piña", "Tropical", 7),
                    ("Kiwi", "Tropical", 14)
                ]

                cur.executemany("INSERT ")