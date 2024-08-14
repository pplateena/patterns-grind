import MATH
import time
def decorator_enter(func):
    def wrapper(*args, **kwargs):
        print("entered function")
        x = func(*args, **kwargs)
        print("exited function")
        return x

    return wrapper
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        z = func(*args, **kwargs)
        time_spent = time.time() - start_time
        return z, time_spent

    return wrapper

@timer
def decorated_sum(a, b):
    sum = MATH.Sum(a, b)
    return sum

def outerSum(*args, **kwargs):

    def inner(*args, **kwargs):
        print("Now in inner function")
        return MATH.Sum(*args, **kwargs)

    print("Entered the outer function")
    start_time = time.time()
    time.sleep(0.3)

    return inner(*args, **kwargs) , time.time() - start_time




if __name__ == 'main':
    print(decorated_sum(12521315, 24317134713456123451)) # Using decorator

    print(outerSum(124, 2)) # Using outer function as decorator