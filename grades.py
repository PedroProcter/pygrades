from models import User, Teacher, Student, Subject, Grade

import sqlite3

student_id = 6

total_grade = 0
n = 0
average = 0
student_grade = []
student_name = []
id_subject_grade = []
subject_name = []
i = 0

# Connect to the database
conn = sqlite3.connect('pygrades.db')

# Create a cursor object
cursor = conn.cursor()

# Execute the SELECT statement
cursor.execute("SELECT * FROM grade")

# Fetch all the rows
rows = cursor.fetchall()

# Print the grades
for row in rows:
    if(student_id == row[2]):
        id_subject_grade.append(row[1])
        student_grade.append(row[4])
        #Calculate the total grade (Sume of all grades)
        total_grade += row[4]
        #Calculate the total of subjects that the student has
        n += 1
        # Calculate the average
        average = total_grade / n

# Close the connection
conn.close()

# Connect to the database
conn = sqlite3.connect('pygrades.db')

# Create a cursor object
cursor = conn.cursor()

# Execute the SELECT statement
cursor.execute("SELECT * FROM student")

# Fetch all the rows
rows = cursor.fetchall()

# Print the grades
for row in rows:
    if(student_id == row[0]):
        student_name.append(row[2])

# Close the connection
conn.close()

# Connect to the database
conn = sqlite3.connect('pygrades.db')

# Create a cursor object
cursor = conn.cursor()

# Execute the SELECT statement
cursor.execute("SELECT * FROM subject")

# Fetch all the rows
rows = cursor.fetchall()

# Print the grades
for row in rows:
    if(id_subject_grade[i] == row[0]):
        subject_name.append(row[1])
        i+= 1

# Close the connection
conn.close()

#Print the name of the student and all the grades
print("Estudiante: ",student_name[0])
print("\n")
# Print the grades
for g in range(2):
    print("Asignatura: ",subject_name[g])
    print("Calificacion: ",student_grade[g])
print("\nEl promedio del estudiante es: ",average)