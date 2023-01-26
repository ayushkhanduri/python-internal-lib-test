import time
from functools import cache, wraps

def func_1(wrapper_fn):
    @wraps(wrapper_fn)
    def inner (*args, **kwargs):
        print("First function start", wrapper_fn.__name__)
        wrapper_fn(*args, **kwargs)
        print("First function end", wrapper_fn.__name__)
    return inner

def func_2(wrapper_fn):
    @wraps(wrapper_fn)
    def inner (*args, **kwargs):
        print("Second function start", wrapper_fn.__name__)
        wrapper_fn(*args, **kwargs)
        print("Second function end", wrapper_fn.__name__)
    return inner


@func_1 #first, func_2 will be passed as an argument for func_1
@func_2 #2nd , testing_function will be passed as an argument for func_2
def testing_function(name):
    print("Printing name: ", name)


testing_function("Ayush")

def execution_time(wrapper_fn):
    def inner(*args, **kwargs):
        start_time = time.time()
        result = wrapper_fn(*args, **kwargs)
        end_time = time.time()
        print(end_time-start_time)
        return result
    return inner

@execution_time
@cache
def calculate_factorial(number):
    print("Executing")
    fact = 1
    for i in range(1,number+1):
        fact *= i
    return fact

# ans = calculate_factorial(100)
# ans2 = calculate_factorial(100)

# print(id(ans))
# print(id(ans2))
