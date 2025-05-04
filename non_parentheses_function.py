def add(a, b):
    return a+b

def cal(a, b, func):
    return func(a, b)

result = cal(3, 5, add)
print(result)
