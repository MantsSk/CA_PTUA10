def operation_logger(func):
    def wrapper(*args, **kwargs):
        operation_name = func.__name__
        result = func(*args, **kwargs)
        print(f"Operation: {operation_name}, Result: {result}")
        return result
    return wrapper

@operation_logger
def add(a, b):
    return a + b

@operation_logger
def subtract(a, b):
    return a - b

@operation_logger
def multiply(a, b):
    return a * b

@operation_logger
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Test the calculator operations
add(5, 3)
subtract(8, 2)
multiply(4, 6)
divide(10, 2)

# Output:
# Operation: add, Input: 5, 3, Result: 8
# Operation: subtract, Input: 8, 2, Result: 6
# Operation: multiply, Input: 4, 6, Result: 24
# Operation: divide, Input: 10, 2, Result: 5.0


