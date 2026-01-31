tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, task)

    elif choice == "3":
        num = int(input("Task number: "))
        if 1 <= num <= len(tasks):
            tasks[num-1] = input("New task: ")
            print("Updated!")
        else:
            print("Invalid number")

    elif choice == "4":
        num = int(input("Task number: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            print("Deleted!")
        else:
            print("Invalid number")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Wrong choice") 