def rate_lecturer(lecturer, student, course, grade):
    if isinstance(lecturer, Lecturer) and isinstance(student, Student) \
            and course in lecturer.courses_attached and course in student.courses_in_progress:
        if course in lecturer.grades:
            lecturer.grades[course] += [grade]
        else:
            lecturer.grades[course] = [grade]
    else:
        return 'Ошибка...'


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def average_grade(self):
        total_grades = 0
        num_grades = 0
        for course_grades in self.grades.values():
            total_grades += sum(course_grades)
            num_grades += len(course_grades)
        if num_grades > 0:
            return round(total_grades / num_grades, 1)
        else:
            return 0.0

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)

        return f"Имя: {self.name}\
                \nФамилия: {self.surname}\
                \nСредняя оценка за домашние задания: {self.average_grade()}\
                \nКурсы в процессе изучения: {courses_in_progress}\
                \nЗавершенные курсы: {finished_courses}"

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, grades=[]):
        super().__init__(name, surname)
        self.grades = grades
        self.grades = {}

    def average_grade(self):
        total_grades = 0
        num_grades = 0
        for course_grades in self.grades.values():
            total_grades += sum(course_grades)
            num_grades += len(course_grades)
        if num_grades > 0:
            return round(total_grades / num_grades, 1)
        else:
            return 0.0

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}"

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка...'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def average_grade_for_course(students, course_name):
    total_grades = 0
    num_grades = 0
    for student in students:
        if course_name in student.grades:
            total_grades += sum(student.grades[course_name])
            num_grades += len(student.grades[course_name])
    if num_grades > 0:
        return round(total_grades / num_grades, 1)
    else:
        return 0.0


def average_grade_for_lecturers(lecturers, course_name):
    total_grades = 0
    num_grades = 0
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            total_grades += sum(lecturer.grades[course_name])
            num_grades += len(lecturer.grades[course_name])
    if num_grades > 0:
        return round(total_grades / num_grades, 1)
    else:
        return 0.0


# Students
best_student = Student('Ruoy', 'Eman', 'men')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в специальность']

worst_student = Student('Jack', 'Olman', 'men')
worst_student.courses_in_progress += ['Python']
worst_student.finished_courses += ['1c']

# Lecturers
cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

strict_lecturer = Lecturer('Sonny', 'Valensia')
strict_lecturer.courses_attached += ['Python']

# Reviewers
nice_reviewer = Reviewer('Bill', 'Winston')
nice_reviewer.courses_attached += ['Python']

cool_reviewer = Reviewer('Bob', 'Smit')
cool_reviewer.courses_attached += ['Python']

# Experiments
rate_lecturer(cool_lecturer, best_student, 'Python', 10)
rate_lecturer(cool_lecturer, best_student, 'Python', 9)
rate_lecturer(strict_lecturer, best_student, 'Python', 8)

rate_lecturer(strict_lecturer, worst_student, 'Python', 1)

cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Python', 10)

nice_reviewer.rate_hw(worst_student, 'Python', 5)

students = [best_student, worst_student]
course_name = "Python"
average_grade_students = average_grade_for_course(students, course_name)
print(f"Средняя оценка студентов за домашние задания по курсу {course_name}: {average_grade_students}")

lecturers = [cool_lecturer, strict_lecturer]
course_name = "Python"
average_grade_lecturers = average_grade_for_lecturers(lecturers, course_name)
print(f"Средняя оценка лекторов за лекции по курсу {course_name}: {average_grade_lecturers}")
