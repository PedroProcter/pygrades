from peewee import SqliteDatabase, Model, AutoField, CharField, BooleanField, ForeignKeyField, SmallIntegerField

db = SqliteDatabase("pygrades.db")

class User(Model):
    id = AutoField(null = False)
    username = CharField(unique = True)
    password = CharField(null = False)
    isTeacher = BooleanField(null = False)

    class Meta:
        database = db

class Teacher(Model):
    id = AutoField(null = False)
    user = ForeignKeyField(User)
    fullname = CharField(null = False)

    class Meta:
        database = db

class Student(Model):
    id = AutoField(null = False)
    user = ForeignKeyField(User)
    fullname = CharField(null = False)

    class Meta:
        database = db

class Subject(Model):
    id = AutoField(null = False)
    name = CharField(null = False)

    class Meta:
        database = db

class Grade(Model):
    id = AutoField(null = False)
    subject = ForeignKeyField(Subject)
    student = ForeignKeyField(Student)
    teacher = ForeignKeyField(Teacher)
    value = SmallIntegerField(null = False)

    class Meta:
        database = db

db.connect()
db.create_tables([
    User,
    Teacher,
    Student,
    Subject,
    Grade,
])
