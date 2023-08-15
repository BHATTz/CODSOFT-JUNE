# Initialize an empty list to store tasks
tasks = []

# Function to display the current tasks
def display_tasks():
    print("Tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")
    print()

# Main loop
while True:
    print("To-Do List Application")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Display Tasks")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter task name: ")
        tasks.append(task_name)
        print("Task added!\n")

    elif choice == "2":
        display_tasks()
        task_idx = int(input("Enter task number to update: ")) - 1
        if 0 <= task_idx < len(tasks):
            new_task_name = input("Enter new task name: ")
            tasks[task_idx] = new_task_name
            print("Task updated!\n")
        else:
            print("Invalid task number!\n")

    elif choice == "3":
        display_tasks()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.\n")
