from typing import TypeVar , Generic

T = TypeVar("T")

class student(Generic[T]):
    def __init__(self, student_id: T, name: str):
        self.student_id = student_id
        self.name = name

    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")


s1 = student[int](100,"john")

s2 = student[str]("STU001","alex")

s1.display()
print("-" * 20)
s2.display()