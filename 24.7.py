class Student:

    school_name = 'ABC School '
    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

s1 = Student('Emma', 10)
print(s1.name, s1.roll_no, Student.school_name)



s2 = Student('Jessa', 20)

print(s2.name, s2.roll_no, Student.school_name)