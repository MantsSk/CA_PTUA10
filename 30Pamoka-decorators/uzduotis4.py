import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        print(f'{func.__name__} took {end - start} to execute.')
        return result
    return wrapper

@execution_time
def my_func():
    return 'This is just a test'

print(my_func())