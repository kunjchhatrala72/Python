import sqlite3




def connect_db():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS students(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       age INTEGER,
                       course TEXT

                   )
                   """)
    conn.commit()
    return conn, cursor

if __name__ == "__main__":
    connect_db()