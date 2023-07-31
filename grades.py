
import sqlite3

student_id:int = 6

#This function enters the data base and gets all the important data of the student
def get_student_data(student_id: int):
    total_grade = 0                 #variable for the sume of all the grades
    n = 0                           #n, to know all the subjects that the student has
    average: float = 0              #this is the average of the sume of all grades divided by the number of subjects
    student_grade = []              #used to storage the grades values
    student_name = []               #used to storage the name of the student
    id_subject_grade = []           #used to storage the id of the subject
    subject_name = []               #used to storage the name of the subject
    teacher_subject_grade_id = []   #id of the teacher that modifies or create the grades
    i:int = 0                       #used for the for statement

    # Connect to the database
    conn = sqlite3.connect('pygrades.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the SELECT statement to enter the grade table
    cursor.execute("SELECT * FROM grade")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the grades
    for row in rows:
        if(student_id == row[2]):
            id_subject_grade.append(row[1])
            teacher_subject_grade_id.append(row[3])
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

    # Execute the SELECT statement to enter the student table
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

    # Execute the SELECT statement to enter the subject table
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

    #Return all the data that is necessary
    return student_name, id_subject_grade, subject_name, student_grade, teacher_subject_grade_id, average

#This function is for show the grades of a student
def show_grades(student_id: int):
    grades = []
    grades = get_student_data(student_id)

    #Print the name of the student and all the grades
    print("Estudiante: ",grades[0])
    print("\n")
    # Print the grades
    for g in range(2):
        print("Asignatura: ",grades[2][g])
        print("Calificacion: ",grades[3][g])

#This function is for show the grades avergae of a student
def show_average(student_id: int):
    grades = []
    grades = get_student_data(student_id)

    print("\nEstudiante: ",grades[0])
    print("Promedio: ",grades[5])


show_grades(student_id)
show_average(student_id)