class A:
    a="welcome to class A"

class B:
    b="welcome to class B"

class C(A,B):
    c="welcome to class C"

c1=C()

print(c1.a)
print(c1.b)
print(c1.c)
