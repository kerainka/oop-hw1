#!/usr/bin/env python
# coding: utf-8

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        average_grade = self.get_average_grade()
        courses_in_progress = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)
        return "Имя: {}\nФамилия: {}\nСредняя оценка за домашнее задание: {}\nКурсы в процессе изучения: {" \
               "}\nЗавершенные курсы: {}".format(self.name, self.surname, average_grade, courses_in_progress, finished_courses)

    def get_average_grade(self):
        total_sum = 0
        total_count = 0
        for grade_list in self.grades.values():
            for grade in grade_list:
                total_sum += grade
                total_count += 1
        if total_count == 0:
            average_grade = 0
        else:
            average_grade = total_sum / total_count
        return average_grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Не студент")
            return
        return self.get_average_grade() < other.get_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        total_sum = 0
        total_count = 0
        for grade_list in self.grades.values():
            for grade in grade_list:
                total_sum += grade
                total_count += 1
        if total_count == 0:
            average_grade = 0
        else:
            average_grade = total_sum / total_count
        return average_grade

    def __str__(self):
        average_grade = self.get_average_grade()
        return "Имя: {}\nФамилия: {}\nСредняя оценка за лекции: {}".format(self.name, self.surname, average_grade)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Не лектор")
            return
        return self.get_average_grade() < other.get_average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return "Имя: {}\nФамилия: {}".format(self.name, self.surname)


def student_average_grade_for_course(students, course):
    total_sum = 0
    total_count = 0
    for student in students:
        for grade in student.grades[course]:
            total_sum += grade
            total_count += 1
    if total_count == 0:
        average_grade = 0
    else:
        average_grade = total_sum / total_count
    print("Средняя оценка за домашние задания по всем студентам в рамках {}: {}".format(course, average_grade))


def lecturer_average_grade_for_course(lecturers, course):
    total_sum = 0
    total_count = 0
    for lecturer in lecturers:
        for grade in lecturer.grades[course]:
            total_sum += grade
            total_count += 1
    if total_count == 0:
        average_grade = 0
    else:
        average_grade = total_sum / total_count
    print("Средняя оценка за лекции всех лекторов в рамках {}: {}".format(course, average_grade))


student_1 = Student("Владимир", "Петров", "м")
student_2 = Student("Кристина", "Орлова", "ж")
lecturer_1 = Lecturer("Питер", "Паркер")
lecturer_2 = Lecturer("Тони", "Старк")
reviewer_1 = Reviewer("Шерлок", "Холмс")
reviewer_2 = Reviewer("Драко", "Малфой")

student_1.courses_in_progress += ["Python", "HTML", "English"]
student_1.finished_courses += ["Javascript"]
student_2.courses_in_progress += ["Python", "HTML"]
student_2.finished_courses += ["Java"]
lecturer_1.courses_attached += ["HTML", "Javascript"]
lecturer_2.courses_attached += ["Python", "Java", "HTML"]
reviewer_1.courses_attached += ["HTML", "Python", "Javascript"]
reviewer_2.courses_attached += ["Java", "CSS"]

student_1.rate_lecturer(lecturer_2, "Python", 8)
student_1.rate_lecturer(lecturer_2, "HTML", 6)
student_2.rate_lecturer(lecturer_2, "Python", 7)
student_2.rate_lecturer(lecturer_1, "HTML", 9)

reviewer_1.rate_hw(student_1, "Python", 10)
reviewer_1.rate_hw(student_2, "Python", 9)
reviewer_1.rate_hw(student_2, "HTML", 7)

print(student_1, end="\n\n")
print(student_2, end="\n\n")
print(lecturer_1, end="\n\n")
print(lecturer_2, end="\n\n")
print(reviewer_1, end="\n\n")
print(reviewer_2, end="\n\n")

print(student_1 > student_2)
print(student_1 < student_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 < lecturer_2, end="\n\n")

student_average_grade_for_course([student_1, student_2], "Python")
lecturer_average_grade_for_course([lecturer_1, lecturer_2], "HTML")



