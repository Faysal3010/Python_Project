def my_decorator(func):
    def wrapper():
        print("Function 1")
        func()
        print("Function 2")
    return wrapper

@my_decorator
def say_hello():
    print("hello!")

say_hello()
