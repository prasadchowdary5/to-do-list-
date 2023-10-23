
import os


def display_tasks(task_list):
    if not task_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(task_list, start=1):
            print(f"{i}. {task}")

def add_task(task_list, task):
    task_list.append(task)
    print(f"Task '{task}' added to the to-do list.")


def remove_task(task_list, index):
    if 1 <= index <= len(task_list):
        removed_task = task_list.pop(index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index. Please try again.")


def save_to_file(task_list, filename):
    with open(filename, 'w') as file:
        for task in task_list:
            file.write(task + '\n')
        print("To-Do List saved to", filename)


def load_from_file(filename):
    task_list = []
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            task_list = [line.strip() for line in file.readlines()]
    return task_list

def main():
    filename = "todo.txt"
    task_list = load_from_file(filename)

    while True:
        print("\nOptions:")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Save To-Do List")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(task_list)
        elif choice == '2':
            task = input("Enter a new task: ")
            add_task(task_list, task)
        elif choice == '3':
            index = int(input("Enter the index of the task to remove: "))
            remove_task(task_list, index)
        elif choice == '4':
            save_to_file(task_list, filename)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
