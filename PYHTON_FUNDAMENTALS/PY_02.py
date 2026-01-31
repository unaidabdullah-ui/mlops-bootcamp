# --- OOP Example: Student Class ---

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def average(self):
        return sum(self.marks) / len(self.marks)
    
    def show(self):
        print(f"Student: {self.name}, Average: {self.average()}")

s1 = Student("Unaid", [90, 85, 88])
s1.show()
