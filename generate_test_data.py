from faker import Faker
import random
import json

def main():

    courses_count = 12
    students_count = 300

    course_records = generate_courses(courses_count)
    student_records = generate_students(students_count, courses_count)

    write_to_file("courses.json",course_records)
    write_to_file("students.json", student_records)



def write_to_file(file_name,data):
    f = open(file_name, "w")
    f.write(data)
    f.close()


def generate_courses(courses_count):

    fake = Faker()

    courses = []
    course_names = []
    lecturers = []

    # Генерация названий курсов и имён лекторов
    for i in range(courses_count):
        course_names.append(fake.word())
        lecturers.append(fake.name())

    # Генерация json объектов
    for i in range(courses_count):
        random_lecturer = lecturers[random.randint(0, courses_count - 1)]
        lecturer_name, lecturer_lastname = random_lecturer.split()[:2]

        course_as_dict = {
            "_id":i,
            "name" : course_names[i] ,
            "lecturer_first_name" : lecturer_name,
            "lecturer_last_name" :lecturer_lastname }

        courses.append(course_as_dict)
    
    return json.dumps(courses)


def generate_students(students_count, courses_count):

    students = []
    groups_count = 3
    fake = Faker()

    # Случайное имя группы 
    groups = [fake.word() for i in range(groups_count)]

    for i in range(students_count):

        # Случайное имя и фамилия студента
        name, lastname = fake.name().split()[:2]
        grades = []

        # Случайное число курсов
        student_courses_count = random.randint(1, courses_count - 1)

        # Генерация курсов студента
        for random_course in random.sample(range(0, courses_count), student_courses_count):
            grades.append({
                "course_id":random_course,
                "grade": random.randint(2, 5)
            })

        # Генерация студентов
        student_as_dict = {
            "first_name": name,
            "last_name": lastname,
            "age": random.randint(10, 100),
            "group": groups[random.randint(0, len(groups) - 1)],
            "grades": grades
        }

        students.append(student_as_dict)

    return json.dumps(students)

if __name__ == "__main__":
    main()