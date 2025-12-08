# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.surname = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.surname = "Hernandez"
    student1.age = 19
    student2.name = "Olivia"
    student2.surname = "Fort"
    student2.age = 21
    student3.name = "Jacob"
    student3.surname = "Darrens"
    student3.age = 22

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.surname} ,{student1.age} years old')
    print(f'{student2.name}, {student2.surname} ,{student2.age} years old')
    print(f'{student3.name}, {student3.surname}, {student3.age}')

if __name__ == "__main__":
    main()