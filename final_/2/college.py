
class College:
    def __init__(self, college_name: str, capacity: int):
        self.college_name = college_name
        self.capacity = capacity
        self.total_students = 0
        self.students = list()

    def get_name_shortcut(self):
        if len(self.college_name) == 0:
            return ""
        words = self.college_name.split(" ")
        shortcut = ""
        for word in words:
            shortcut += (word[0])
        return shortcut

    def update_total_students(self, student):
        if self.total_students + 1 > self.capacity:
            return False
        else:
            self.total_students += 1
            self.students.append(student)
            return True

    def get_info(self):
        print(f"{self.college_name} ({self.get_name_shortcut()}) "
              f"with ({self.total_students} out of {self.capacity})")
        for student in self.students:
            student.get_info()
