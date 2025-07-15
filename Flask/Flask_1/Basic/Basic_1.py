def smart_decorator(func):
    def wrapper(name):
        print("Decorated Function run...")
        func(name)
    return wrapper

@smart_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Faysal")