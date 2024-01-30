def ascii_art_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        ascii_art_result = ""
        for char in str(result):
            ascii_art_result += f" {char} "
        
        border = "+" + "-" * (len(ascii_art_result)) + "+"
        decorated_result = f"{border}\n|{ascii_art_result}|\n{border}"

        return decorated_result
    return wrapper

@ascii_art_decorator
def generate_pattern():
    return "Decorated"

result = generate_pattern()
print(result)
