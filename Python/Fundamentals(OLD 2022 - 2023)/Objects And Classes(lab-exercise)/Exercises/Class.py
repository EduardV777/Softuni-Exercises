class Class:
    __students_count=22
    def __init__(self,name):
        self.name=name
        self.students=[]
        self.grades=[]
    def add_student(self,name: str, grade: float):
        if len(self.students)<self.__students_count:
            self.students.append(name); self.grades.append(grade)
    def get_average_grade(self):
        avgGrades=0
        for k in range(0,len(self.grades)):
            avgGrades+=self.grades[k]
        avgGrades/=len(self.grades)
        return f"{avgGrades:.2f}"
    def __repr__(self):
        avgGrade=self.get_average_grade()
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {avgGrade}"

# a_class = Class("11B")
# a_class.add_student("Peter", 4.80)
# a_class.add_student("George", 6.00)
# a_class.add_student("Amy", 3.50)
# print(a_class)
