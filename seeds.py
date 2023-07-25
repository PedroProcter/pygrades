from peewee import SqliteDatabase

from models import User, Teacher, Student, Subject, Grade



def main():

    db = SqliteDatabase("pygrades.db")
    db.connect()
    db.create_tables([
        User,
        Teacher,
        Student,
        Subject,
        Grade,
    ])

    #Teachers
    first_user = User(username = "Juan Rosario", password = "JuanRosario1", isTeacher = True)
    first_user.save()

    teacher = Teacher(fullname = "Juan Rosario", user = first_user)
    teacher.save()

    second_user = User(username = "Maria Sanchez", password = "MariaSanchez1", isTeacher = True)
    second_user.save()

    teacher = Teacher(fullname = "Maria Sanchez", user = second_user)
    teacher.save()

    third_user = User(username = "Leonardo Paredes", password = "LeonardoParedes1", isTeacher = True)
    third_user.save()

    teacher = Teacher(fullname = "Leonardo Paredes", user = third_user)
    teacher.save()

    fourth_user = User(username = "Jennifer Lopez", password = "JenniferLopez1", isTeacher = True)
    fourth_user.save()

    teacher = Teacher(fullname = "Jennifer Lopez", user = fourth_user)
    teacher.save()

    fifth_user = User(username = "Miguel Dante", password = "MiguelDante1", isTeacher = True)
    fifth_user.save()

    teacher = Teacher(fullname = "Miguel Dante", user = fifth_user)
    teacher.save()

    #Students
    sixth_user = User(username = "Pedro Procter", password = "PedroProcter1", isTeacher = False)
    sixth_user.save()

    student = Student(fullname = "Pedro Procter", user = sixth_user)
    student.save()

    seventh_user = User(username = "Guarino Mendoza", password = "GuarinoMendoza1", isTeacher = False)
    seventh_user.save()

    student = Student(fullname = "Guarino Mendoza", user = seventh_user)
    student.save()

    eighth_user = User(username = "Arnaldo Pena", password = "ArnaldoPena1", isTeacher = False)
    eighth_user.save()

    student = Student(fullname = "Arnaldo Pena", user = eighth_user)
    student.save()

    ninth_user = User(username = "Diego Garabito", password = "DiegoGarabito1", isTeacher = False)
    ninth_user.save()

    student = Student(fullname = "Diego Garabito", user = ninth_user)
    student.save()

    tenth_user = User(username = "Miguel Santos", password = "MiguelSantos1", isTeacher = False)
    tenth_user.save()

    student = Student(fullname = "Miguel Santos", user = tenth_user)
    student.save()

    eleventh_user = User(username = "Gabriela Moreno", password = "GabrielaMoreno1", isTeacher = False)
    eleventh_user.save()

    student = Student(fullname = "Gabriela Moreno", user = eleventh_user)
    student.save()

    twelfth_user = User(username = "Santiago Leon", password = "SantiagoLeon1", isTeacher = False)
    twelfth_user.save()

    student = Student(fullname = "Santiago Leon", user = twelfth_user)
    student.save()

    thirteenth_user = User(username = "Marie Camilo", password = "MarieCamilo1", isTeacher = False)
    thirteenth_user.save()

    student = Student(fullname = "Marie Camilo", user = thirteenth_user)
    student.save()

    fourteenth_user = User(username = "Frank Rodriguez", password = "FrankRodriguez1", isTeacher = False)
    fourteenth_user.save()

    student = Student(fullname = "Frank Rodriguez", user = fourteenth_user)
    student.save()

    fifteenth_user = User(username = "Michelle Perez", password = "MichellePerez1", isTeacher = False)
    fifteenth_user.save()

    student = Student(fullname = "Michelle Perez", user = fifteenth_user)
    student.save()

    sixteenth_user = User(username = "David Luciano", password = "DavidLuciano1", isTeacher = False)
    sixteenth_user.save()

    student = Student(fullname = "David Luciano", user = sixteenth_user)
    student.save()

    seventeenth_user = User(username = "Carmen Marte", password = "CarmenMarte1", isTeacher = False)
    seventeenth_user.save()

    student = Student(fullname = "Carmen Marte", user = seventeenth_user)
    student.save()

    eighteenth_user = User(username = "Lisa Matos", password = "LisaMatos1", isTeacher = False)
    eighteenth_user.save()

    student = Student(fullname = "Lisa Matos", user = eighteenth_user)
    student.save()

    #Subjects
    first_subject = Subject(name = "Arte")
    first_subject.save()

    second_subject = Subject(name = "Matematicas")
    second_subject.save()

    #third_subject = Subject(name = "Ciencias Sociales")
    #third_subject.save()

    #fourth_subject = Subject(name = "Ciencias Naturales")
    #fourth_subject.save()

    #fifth_subject = Subject(name = "Historia")
    #fifth_subject.save()

    #sixth_subject = Subject(name = "Ingles")
    #sixth_subject.save()

    #seventh_subject = Subject(name = "Informatica")
    #seventh_subject.save()

    #eighth_subject = Subject(name = "Educacion Fisica")
    #eighth_subject.save()

    #Grades
    first_grade_first_student = Grade(subject = 1, student = 1, teacher = 3, value = 85)
    first_grade_first_student.save()

    second_grade_first_student = Grade(subject = 2, student = 1, teacher = 1, value = 95)
    second_grade_first_student.save()

    first_grade_second_student = Grade(subject = 1, student = 2, teacher = 3, value = 90)
    first_grade_second_student.save()

    second_grade_second_student = Grade(subject = 2, student = 2, teacher = 1, value = 95)
    second_grade_second_student.save()

    first_grade_third_student = Grade(subject = 1, student = 3, teacher = 3, value = 80)
    first_grade_third_student.save()

    second_grade_third_student = Grade(subject = 2, student = 3, teacher = 1, value = 80)
    second_grade_third_student.save()

    first_grade_fourth_student = Grade(subject = 1, student = 4, teacher = 3, value = 85)
    first_grade_fourth_student.save()

    second_grade_fourth_student = Grade(subject = 2, student = 4, teacher = 1, value = 85)
    second_grade_fourth_student.save()

    first_grade_fifth_student = Grade(subject = 1, student = 5, teacher = 3, value = 90)
    first_grade_fifth_student.save()

    second_grade_fifth_student = Grade(subject = 2, student = 5, teacher = 1, value = 90)
    second_grade_fifth_student.save()

    first_grade_sixth_student = Grade(subject = 1, student = 6, teacher = 3, value = 100)
    first_grade_sixth_student.save()

    second_grade_sixth_student = Grade(subject = 2, student = 6, teacher = 1, value = 100)
    second_grade_sixth_student.save()

    first_grade_seventh_student = Grade(subject = 1, student = 7, teacher = 3, value = 75)
    first_grade_seventh_student.save()

    second_grade_seventh_student = Grade(subject = 2, student = 7, teacher = 1, value = 70)
    second_grade_seventh_student.save()

    first_grade_eighth_student = Grade(subject = 1, student = 8, teacher = 3, value = 88)
    first_grade_eighth_student.save()

    second_grade_eighth_student = Grade(subject = 2, student = 8, teacher = 1, value = 93)
    second_grade_eighth_student.save()

    first_grade_ninth_student = Grade(subject = 1, student = 9, teacher = 3, value = 86)
    first_grade_ninth_student.save()

    second_grade_ninth_student = Grade(subject = 2, student = 9, teacher = 1, value = 89)
    second_grade_ninth_student.save()

    first_grade_tenth_student = Grade(subject = 1, student = 10, teacher = 3, value = 91)
    first_grade_tenth_student.save()

    second_grade_tenth_student = Grade(subject = 2, student = 10, teacher = 1, value = 81)
    second_grade_tenth_student.save()


if __name__ == "__main__":
    main()
