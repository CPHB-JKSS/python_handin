import random
import csv


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

    def add_new_course(self, course):
        self.courses[course] = course.grade


class Course():
    def __init__(self, name, classroom, teacher, ects, grade="N/A"):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ects = ects
        self.grade = grade

    def set_grade(self, grade):
        self.grade = grade


def main():
    generate_students(5, '../files/students.csv')
    print(read_student_data('../files/students.csv'))


def generate_students(n, file_path):
    course_names = ("English", "Danish", "Math", "Physics", "Sports")
    course_classrooms = ("11", "12", "13", "21", "22", "23")
    course_teachers = ("John", "Magnus", "Borat", "Sally")
    course_ects = ("5", "10")
    course_grades = (-3, 0, 2, 4, 7, 10, 12)

    names_dict = {
        "Allyn": "male",
        "Aly": "female",
        "Penn": "female",
        "Marley": "female",
        "Kami": "female",
        "Rasmus": "male",
        "Paul": "male",
        "Ben": "male",
        "Annie": "female",
        "George": "male",
    }

    selected_names = random.sample(list(names_dict.items()), k=n)
    students = []
    for name, gender in selected_names:
        student_name = name
        gender = gender
        course_list = random.sample(
            course_names, random.randrange(1, len(course_names))+1)

        courses = []
        for course in course_list:
            courses.append(Course(
                course,
                random.choice(course_classrooms),
                random.choice(course_teachers),
                random.choice(course_ects),
                random.choice(course_grades)
            ))
        data_sheet = DataSheet(courses)

        students.append(
            Student(student_name, gender, data_sheet, "https://url.com/" + name + ".png"))

    with open(file_path, mode="w") as students_file:
        student_writer = csv.writer(
            students_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        student_writer.writerow([
            'stud_name',
            'course_name',
            'teacher',
            'ects',
            'classroom',
            'grade',
            'img_url'
        ])
        for student in students:
            for stud_course in student.data_sheet.courses:
                student_writer.writerow([
                    student.name,
                    stud_course.name,
                    stud_course.teacher,
                    stud_course.ects,
                    stud_course.classroom,
                    stud_course.grade,
                    student.image_url
                ])


def read_student_data(input_file):
    students = []

    with open(input_file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if len(row) > 0:
                stud_name = row[0]
                course_name = row[1]
                teacher = row[2]
                ects = row[3]
                classroom = row[4]
                grade = row[5]
                img_url = row[6]

                if line_count == 0:
                    #print(f'Columns: {", ".join(row)}')
                    line_count += 1
                else:
                    for student in students:
                        if stud_name not in student.name:
                            course = Course(
                                course_name, classroom, teacher, ects, grade
                            )
                            data_sheet = DataSheet([course])
                            students.append(
                                Student(stud_name, "N/A", data_sheet, img_url)
                            )
                        else:
                            course = Course(
                                course_name, classroom, teacher, ects, grade
                            )
                            student.data_sheet.add_new_course(course)

                    #print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}')
                    line_count += 1
    return students


if __name__ == '__main__':
    main()
