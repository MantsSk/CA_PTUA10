class Task:
    def __init__(self, description, status="To Do"):
        self.description = description
        self.status = status

    def display_info(self):
        print(f"Task: {self.description}")
        print(f"Status: {self.status}")
        print("--------------------")

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.description}' added to the To-Do List.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the To-Do List.")
        else:
            print("To-Do List:")
            for task in self.tasks:
                task.display_info()

    def mark_as_done(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                task.status = "Done"
                print(f"Task '{task.description}' marked as Done.")
                return
        print(f"Task '{task_description}' not found in the To-Do List.")

todo_list = ToDoList()

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Done")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task_description = input("Enter task description: ")
        new_task = Task(task_description)
        todo_list.add_task(new_task)

    elif choice == "2":
        todo_list.display_tasks()

    elif choice == "3":
        task_description = input("Enter task description to mark as done: ")
        todo_list.mark_as_done(task_description)

    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
