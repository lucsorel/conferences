'''
source .venv/bin/activate
cd examples
py2puml doc_as_code doc_as_code > doc_as_code/doc_as_code.puml
'''
from dataclasses import dataclass

@dataclass
class Person:
    firstname: str
    lastname: str

@dataclass
class Course:
    name: str
    teacher: Person

@dataclass
class Student(Person):
    courses: list[Course]