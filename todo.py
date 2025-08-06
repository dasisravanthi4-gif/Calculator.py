tasks = []

while True:
    choice = input("\nAdd/View/Exit: ").lower()

    if choice == "add":
        tasks.append(input("Enter task: "))
    elif choice == "view":
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    elif choice == "exit":
        break
    else:
        print("Invalid option.")
