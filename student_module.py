class Student:
    
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def get_all_marks(self):
        return self.marks

    def calc_average(self):
        average = sum(self.marks) / len(self.marks)
        return average

