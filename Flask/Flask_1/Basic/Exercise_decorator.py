import time
current_time = time.time()
print(f"current time: {current_time}") # start from 1970, jan 1

def speed_calc_decorator(func):
    def wrapper():
        start_time=time.time()
        print(f"Start time: {start_time}")
        func()
        end_time=time.time()
        print(f"end Time: {end_time}")
        print(func.__name__,end_time-start_time)
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i # type: ignore
    
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i # type: ignore

fast_function()
slow_function()






# import time

# print(time.time()) 
# def cal_time_decorator(func):
#     def wrapper():
#         start_time=time.time()
#         func()
#         end_time=time.time()
#         print(f"{func.__name__} : {end_time-start_time}")
#     return wrapper

# @cal_time_decorator
# def fast_time():
#     for i in range(10000000):
    #    i*i*i  change to pass/i/i*i......

        
# @cal_time_decorator
# def slow_time():
#     for i in range(100000000):
#        i*i*i  change to pass/i/i*i......

# fast_time()
# slow_time()