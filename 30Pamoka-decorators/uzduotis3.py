todo_list = []

def print_todo(func):
    def wrapper(*args, **kwargs):
        print("Current To-Do List:", todo_list)
        result = func(*args, **kwargs)
        print("Updated To-Do List:", todo_list)
        return result
    return wrapper

@print_todo
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

@print_todo
def complete_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' marked as completed.")
    else:
        print(f"Task '{task}' not found in the to-do list.")

# Test the to-do list functions
add_task("Buy groceries")
add_task("Finish project")
print_todo()
complete_task("Buy groceries")
