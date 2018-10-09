# create a class including the same attribution for various subject.

class student:
    def __init__(self, name, age, gender,gpa):
        self.name = name
        self.age = age
        self.gender = gender
        self.gpa = gpa

# build a function to describe the value
    def on_roll(student):
        if student.gpa > 3:
            return True
        else:
            return False