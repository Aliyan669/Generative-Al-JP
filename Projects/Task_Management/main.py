task = []
print("Welcome to the Task Management App.......")

today_task = int(input("Enter How Many Task you want to Add= "))

for i in range(1, today_task+1):
    task_name = input(f"Enter Task {i}= ")
    task.append(task_name)

print("Today Task are", task)

while True:
    operation = int(
        input("Enter 1) Add \n 2) Update \n 3) Delete \n 4) View \n 5) Exit & Stop "))
    if operation == 1:
        add = input("Enter Task you want to Add= ")
        task.append(add)
        print("Task", add, "has been Successfully Added")

    elif operation == 2:
        update_val = input("Enter Task you want to Update = ")
        if update_val in task:
            update = input("Enter New Task")
            ind = task.index(update_val)
            task[ind] = update
            print("Updated Task", update)

    elif operation == 3:
        del_val = input("Enter Task you want to Delete = ")
        if del_val in task:
            ind = task.index(del_val)
            del task[ind]
            print("Deleted Task", del_val)

    elif operation == 4:
        print("Today Total Task are", task)

    elif operation == 5:
        print("Closing the Program......")
        break

    else:
        print("Invalid Input")
