import sqlite3
subject_id = 2

def get_data(subject_id: int):
    subject_name = []
    subject_id = []
    conn = sqlite3.connect('pygrades.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subject")
    rows = cursor.fetchall()
    for row in rows:
        subject_id.append(row[0])
        subject_name.append(row[1])
    conn.close()

    return subject_name, subject_id

def show_subject():
    conn = sqlite3.connect('pygrades.db')
    cursor = conn.cursor()
    sqlcount = "SELECT COUNT(*) FROM subject"
    cursor.execute(sqlcount)
    cantidad = cursor.fetchone()[0]
    subject = []
    subject= get_data(subject_id)

    for g in range(cantidad):
        print("ID de la materia: ", subject[1][g])
        print("Nombre de la asginatura: ", subject[0][g])

def create_subject():
    show_subject()
    conn = sqlite3.connect('pygrades.db')
    subject_name = input("Ingresa el nombre de la asignatura que desea crear: ")
    sql = "INSERT INTO subject(name) VALUES(?)"
    cursor = conn.cursor()
    cursor.execute(sql, (subject_name,))
    print("Asignatura creada correctamente!!!")
    conn.commit()
    conn.close()

#def edit_subject():
    #show_subject()
    # Create a connection to the database
   # conn = sqlite3.connect('pygrades.db')
    #edit_id = input("Ingrese el id de la asignatura que desea editar: ")
    #cursor = conn.cursor()

    # Execute a SQL statement to select the subject you want to edit
    #cursor.execute('SELECT * FROM subject WHERE id = ?', (subject_id,))

    # Use the cursor object to update the subject's information
    #cursor.execute('UPDATE subject SET name = ?, description = ? WHERE id = ?', (subject_id, new_name))

    # Execute a SQL statement to commit the changes to the database
    #conn.commit()

    # Close the connection to the database
    #conn.close()

def Elimnar_subject():
    show_subject()
    conn = sqlite3.connect('pygrades.db')
    id_eliminar = input("Ingrese el id de la asignatura que desea eliminar: ")
    sql = "DELETE FROM subject WHERE id = ?"
    cursor = conn.cursor()
    cursor.execute(sql, (id_eliminar,))
    print("Asignatura eliminada correctamente!!!")
    conn.commit()
    conn.close()

#Elimnar_subject()
show_subject()
create_subject()
show_subject()
