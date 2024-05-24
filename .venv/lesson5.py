from lesson4 import Teacher, teacher, Student, student, Worker, worker
from inspect import signature

print("\nAttributes Teacher:")
attrs = dir(teacher)
for attr in attrs:
    if not attr.startswith('_') and not callable(getattr(teacher, attr)):
        print(attr)

print("\nMethods Teacher:")
for attr in attrs:
    if not attr.startswith('_') and callable(getattr(teacher, attr)):
        print(attr)

print("\nAttributes Student:")
attrs = dir(student)
for attr in attrs:
    if not attr.startswith('_') and not callable(getattr(student, attr)):
        print(attr)

print("\nMethods Student:")
for attr in attrs:
    if not attr.startswith('_') and callable(getattr(student, attr)):
        print(attr)

print("\nAttributes Worker:")
attrs = dir(worker)
for attr in attrs:
    if not attr.startswith('_') and not callable(getattr(worker, attr)):
        print(attr)

print("\nMethods Worker:")
for attr in attrs:
    if not attr.startswith('_') and callable(getattr(worker, attr)):
        print(attr)