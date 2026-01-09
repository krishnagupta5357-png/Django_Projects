class SSC:
    def info(self):
        print("This Class for the Tenth's Student")
    def add(self):
        a="DIV-A"
        print(a)
s1=SSC()
s1.info()
s1.add()

#Constructor Class:
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("name:", self.name)
        print("marks:", self.marks)
s1 = Student("Krishna", 80)
s2 = Student("Axar", 75)
s3 = Student("Riya", 64)
s1.display()
s2.display()
s3.display()
