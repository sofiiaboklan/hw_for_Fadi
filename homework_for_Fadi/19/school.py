class Person:
    def __init__(self, firstname: str, surname: str, age: int, sex: str):
        self.firstname = firstname
        self.surname = surname
        self.age = age
        self.sex = sex

    def __str__(self) -> str:
        return f"Hello! My name is {self.firstname} {self.surname}, I am a {self.sex} and I am {self.age} years old."


class Student(Person):
    played_hooky_amount = 0

    def __init__(self, firstname: str, surname: str, age: int, sex: str):
        self.grades = {"English": 0, "Math": 0}
        super().__init__(firstname, surname, age, sex)

    def played_hooky(self, amount: int):
        self.played_hooky_amount += amount


class Teacher(Person):

    def __init__(self, firstname: str, surname: str, age: int, sex: str, subject: str, salary: int):
        self.subject = subject
        self.salary = salary
        super().__init__(firstname, surname, age, sex)

    def grade_paper(self, student: Student, grade: int):
        student.grades[self.subject] = grade


# sofiia = Student("Sofiia", "Boklan", 20, "female")
# print(sofiia.__str__())
# sofiia.played_hooky(20)
# print(sofiia.played_hooky_amount)
#
# daniil = Student("Daniil", "Fedorov", 20, "male")
# print(daniil.__str__())
# daniil.played_hooky(10)
# print(daniil.played_hooky_amount)
#
# misha = Teacher("Mykhailo", "Stolnikovych", 22, "male", "English", 50000)
# print(misha.__str__())
# misha.grade_paper(sofiia, 12)
# misha.grade_paper(daniil, 10)
#
# prosha = Teacher("Prokhor", "Mosin", 19, "male", "Math", 20000)
# print(prosha.__str__())
# prosha.grade_paper(sofiia, 2)
# prosha.grade_paper(daniil, 11)
#
# print(sofiia.grades)
# print(daniil.grades)