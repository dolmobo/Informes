import os
import sqlite3

class DataSource:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, "database.db")

    def get_connection():
        conn = sqlite3.connect(DataSource.DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn

    def ensure_db():
        with DataSource.get_connection() as conn:
            cur = conn.cursor()

            # Creación de tablas
            cur.execute("""
                CREATE TABLE IF NOT EXISTS participants (
                    name TEXT NOT NULL,
                    department TEXT NOT NULL,
                    points INTEGER NOT NULL
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS jugadores (
                    name TEXT NOT NULL,
                    team TEXT NOT NULL,
                    age INTEGER NOT NULL
                )
            """)

            conn.commit()

            # Comprobaciones e Inserciones
            cur.execute("SELECT COUNT(*) FROM participants")
            count = cur.fetchone()[0]

            cur.execute("SELECT COUNT (*) FROM jugadores")
            count_player = cur.fetchone()[0]

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
                cur.executemany("INSERT INTO participants VALUES (?,?,?)", sample)
            
            if count_player == 0:
                ins = [
                    ("Antonio", "G2", 18),
                    ("Marcos", "KOI", 20),
                    ("Lucas", "G2", 19),
                    ("Daniel", "G2", 22),
                    ("David", "G2", 24)
                ]
                cur.executemany("INSERT INTO jugadores VALUES (?,?,?)", ins)
                
            conn.commit()

    def obtener_participants():
        with DataSource.get_connection() as conn:

            cur = conn.cursor()
            cur.execute("SELECT * FROM participants ORDER BY department, name")
            return [dict(filas) for filas in cur.fetchall()]
        
    def obtener_jugadores():
        with DataSource.get_connection() as conn:

            cur = conn.cursor()
            cur.execute("SELECT * FROM jugadores ORDER BY team, age")
            return [dict(filas) for filas in cur.fetchall()]
        
    def suma_puntos(rows):
        total = len(rows)
        if rows:
            suma = sum(int(fila["points"]) for fila in rows)
        else:
            suma = 0 
        
        return total, suma
    
    def suma_edad(rows):
        total = len(rows)
        if rows:
            suma_edades = sum(int(fila["age"]) for fila in rows)
        else:
            suma_edades = 0
        return total, suma_edades