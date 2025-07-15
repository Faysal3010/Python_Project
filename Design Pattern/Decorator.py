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

say_bye()
say_hello()