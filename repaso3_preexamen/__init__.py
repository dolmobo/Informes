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

            cur.execute("")
            cur.execute("")

            cur.execute("""
                
                        """)
            
            cur.execute("""
                
                        """)
            
            conn.commit()

            empleados = [
                
            ]

            cur.executemany("")

            jornadas = [
                
            ]

            cur.executemany("", jornadas)

            conn.commit()
    
    def obtener_informacion():
        with DataSource.get_connection() as conn:
            cur: sqlite3.Cursor = conn.cursor()

            cur.execute("""

                        """)
            
            return[ dict(filas) for filas in cur.fetchall() ]
 