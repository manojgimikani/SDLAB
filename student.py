
class student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print("name:",self.name)
        print("roll_no:",self.roll_no)
        print("marks:",self.marks)
    def grade(self):
        if self.marks >= 50:
            return "pass"
        else:
            return "fail"
student1=student("manoj",11,90)
student1.display()
print("result:",student1.grade())
    
        