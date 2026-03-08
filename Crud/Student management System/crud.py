from database import connect_db

# Add student / create

def add_student(name,age,course):
    conn, cursor = connect_db()
    cursor.execute("INSERT INTO students(name,age,course) VALUES (? , ? , ?)",(name, age, course))
    conn.commit()
    cursor.close()
    

# View student  
  
def view_students():
    conn, cursor = connect_db()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No students found")

    conn.close()
    
# Update

def update_student(id,name):
    cursor,conn = connect_db()
    cursor.execute("UPDATE students SET name=? WHERE id=?",(name,id))
    cursor.commit()
    cursor.close()
    
    
# Delete

def delet_student(id):
    cursor,conn = connect_db()
    cursor.execute("DELETE FROM students WHERE id=?",(id,))
    cursor.commit()
    cursor.close()
    
    
    
        
    