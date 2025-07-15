import time


def delay_decorator(function):
    def wrapper():
        time.sleep(2)
        function()
        function()
        # function()
    return wrapper


@delay_decorator
def say_hello():
    print("Hello!")


def say_bye():
    print("Bye!")


def greeting():
    print("Hi!")



say_bye()
say_hello()

delay_decorator_x=delay_decorator(greeting)
delay_decorator_x()


