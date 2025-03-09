import time
from time import sleep
from functools import  wraps
#1
def run_time(func):
    def wrapper(*arg, **kwargs):
        start = time.time()
        sleep(0.5)
        func(*arg,**kwargs)
        end= time.time()
        print(f"run time: {end-start}")
    return  wrapper



@run_time
def f1():
    print("f1")

@run_time
def f2():
    print("f2")
    for _ in range(100000):
        pass

@run_time
def f3():
    print("f3")
    for _ in range(1000000):
        for _ in range(10):
            pass

f1()
f2()
f3()

#2

def cache_memory(func):
    cache = {}
    @wraps(func)
    def wrapper(*arg, **kwargs):
        if arg in cache :
            return cache[arg]
        result = func(*arg, **kwargs)
        cache[arg]=result
        return result
    return wrapper

@run_time
def fibonacci_with_not_cache(n):
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    for _ in range(n - 2):
        c = a + b
        a = b
        b = c
    return c

@run_time
@cache_memory
def fibonacci_with_cache(n):
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    for _ in range(n - 2):
        c = a + b
        a = b
        b = c
    return c

print("fibonacci_with_not_cache")
fibonacci_with_not_cache(35)
print("fibonacci_with_cache")
fibonacci_with_cache(35)