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

    first_user = User(username = "student", password = "dev", isTeacher = False)
    first_user.save()

    student = Student(fullname = "Juan Rosario", user = first_user)
    student.save()

    second_user = User(username = "teacher", password = "dev", isTeacher = True)
    second_user.save()

    teacher = Teacher(fullname = "Maria Sanchez", user = second_user)
    teacher.save()



if __name__ == "__main__":
    main()
