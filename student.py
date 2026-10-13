
class student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("name:", self.name)
        print("roll_no:", self.roll_no)

# Object creation
student1 = student("manoj", 101)
student1.display()
    
        