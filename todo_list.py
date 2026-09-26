def print_menu():
    print("\nTodo List Menu:")

    choices = ["1. View Tasks", "2. Add a Task", "3. Remove a Task", "4. Exit"]
    for choice in choices:
        print(choice)

def get_choice():
    while True:
        choice = input("Enter your choice: ")
        valid_choices = ("1", "2", "3", "4")
            
        if choice not in valid_choices:
            print("Invalid choice")
            continue

        return choice

def display_task(tasks):
    if not tasks:
       print("No tasks in the list.")
       return 

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
        
def add_task(tasks):
    while True:
        task = input("Enter a new task: ").strip()
            
        if task:
            tasks.append(task) 
            break
        
        print("Invalid task")

def remove_task(tasks):    
    while True:
        try:
            task_number = int(input("Enter the task number: ").strip())
                
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid task number")

def main():
    tasks = []

    while True:
        print_menu()

        choice = get_choice()
        if choice == "1":
            display_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            break

if __name__ == "__main__":
    main()