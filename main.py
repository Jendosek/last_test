#10
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

get_info = Student(name = "Zhenia", age=16)
print(f"Ім'я студента: {get_info.name}")
print(f"Вік студента: {get_info.age}")

