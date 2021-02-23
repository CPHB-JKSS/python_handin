import random


def generate_students(n):
    course_names = ("English", "Danish", "Math", "Physics", "Sports")
    course_classrooms = ("11", "12", "13", "21", "22", "23")
    course_teachers = ("John", "Magnus", "Borat", "Sally")
    course_etcs = ("5", "10")
    course_grades = (-3, 0, 2, 4, 7, 10, 12)

    names = ("Allyn", "Aly", "Penn", "Marley", "Kami", "Vix")
    genders = ("male", "female")

    students = []
    for i in range(n):
        name = random.choice(names)
        gender = random.choice(genders)
        course_list = random.choices(course_names)

        courses = []
        for course in course_list:
            courses.append(Course(
                course,
                random.choice(course_classrooms),
                random.choice(course_teachers),
                random.choice(course_etcs),
                random.choice(course_grades)
            ))
        data_sheet = DataSheet(courses)

        students.append(
            Student(name, gender, data_sheet, "https://url.com/" + name + ".png"))

    for student in students:
        student.print_student()


class Student():
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        print()

    def print_student(self):
        print("Student: " + self.name + ", " + self.gender +
              ", " + self.image_url + ", " + self.image_url)


class DataSheet():
    def __init__(self, courses):
        self.courses = {course: course.grade for course in courses}

    def get_grades_as_list(self):
        return self.courses.values()


class Course():
    def __init__(self, name, classroom, teacher, etcs, grade="N/A"):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.etcs = etcs
        self.grade = grade

    def set_grade(self, grade):
        self.grade = grade


def main():
    generate_students(5)


if __name__ == '__main__':
    main()
