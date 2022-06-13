from datetime import date

from person import Person


class Student(Person):
    students = 0

    def __init__(self, first_name: str, middle_name: str, last_name: str,
                 date_of_birth: str, gender: int,
                 identity: str, mobile_number: str):
        super().__init__(first_name, middle_name, last_name, date_of_birth,
                         gender, identity, mobile_number)

        if self.get_age() < 18:
            print("Illegible Age")
            return

        today = date.today()
        zeros = "0" * (4 - (len(str(Student.students))))
        self.student_number = f"{self.gender}{today.year}{zeros}{Student.students}"
        Student.students += 1
        self.college = None

    def set_college(self, college):
        if college.update_total_students(self):
            self.college = college
            print(f"Student Registered Successfully in {college.college_name}"
                  f" {college.get_name_shortcut()}")
        else:
            print(f"{college.college_name} is full try another college :(")

    def get_info(self):
        print(f"{self.first_name} {self.middle_name} {self.last_name}")
        print(f"ID: {self.student_number}")
