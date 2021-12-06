class Class:
    students = []
    grades=[]
    __students_count=22
    def __init__(self, name):
        self.className=name
    def add_student(self,nameStr: str,grade: float):
        if self.__students_count>0:
            self.students.append(nameStr)
            self.grades.append(grade)
    def get_average_grade(self):
        gradeCount=len(self.grades); gradeSum=0
        for k in range(0,len(self.grades)):
            gradeSum+=self.grades[k]
        avg=gradeSum/gradeCount
        return f"{avg:.2f}"
    def __repr__(self):
        return f"The students in {self.className}: {', '.join(self.students)}.\nAverage grade: {self.get_average_grade()}"

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
