from uuid import uuid4
class Student:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.id = uuid4()
        self.grades = []
    
    def add_grade(self, *grades):
        for grade in grades:
            self.grades.append(grade)
    
    def get_average(self):
        return sum(self.grades) / len(self.grades)

    def info(self):
        return f"Name : {self.name}, Lastname : {self.lastname}, Student id : {self.id} "
    
    

class StudentManager:
    def __init__(self):
        self.students = []
 
    def add_student(self, student):
        self.students.append(student)
    
    def remove_student(self, student):
        self.students.remove(student)

    def get_top_student(self):
        return max(self.students, key=Student.get_average)
    
    def get_all_students_sorted(self):
        return sorted(self.students, key=lambda s: s.get_average(), reverse=True)
    
    def get_failing_students(self):
        failing = []
        for student in self.students:
            if student.get_average() < 60:
                failing.append(student.info())
        return failing

    def get_all_student(self):
        return [student.info() for student in self.students]
    
    def get_student_by_name(self, sname):
        for student in self.students:
            if student.name == sname:
                return student.info()
        return "Student not found!"

            
student3 = Student("Bobby", "Charlton")
student3.add_grade(60, 49, 55, 50)
student1 = Student("Baxtiyor", "Xolmo'minov")
student2 = Student("Jack", "Jason")
student1.add_grade(80, 80, 90, 100)
student2.add_grade(79, 70, 90, 60)
manager = StudentManager()
manager.add_student(student1)
manager.add_student(student2)
manager.add_student(student3)
# top = manager.get_top_student()
# print(top.info())
# print(manager.get_all_student())
# manager.remove_student(student2)
# print(manager.get_all_student())

# sorted_students = manager.get_all_students_sorted()
# for student in sorted_students:
#     print(f"{student.name} — {student.get_average()}")
# print(manager.get_failing_students())
#-
# failing = manager.get_failing_students()
# for student in failing:
#     print(student.info())
print(manager.get_student_by_name("Baxtiyor"))
print(manager.get_student_by_name("kai"))