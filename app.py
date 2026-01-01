
import os

class Todo:
    """Represents a single todo item."""
    def __init__(self, task, completed=False):
        self.task = task
        self.completed = completed

    def __str__(self):
        status = "[X]" if self.completed else "[ ]"
        return f"{status} {self.task}"

todos = []

def add_todo():
    """Adds a new todo item."""
    task = input("Enter the task: ")
    todos.append(Todo(task))
    print("Todo added successfully.")

def list_todos():
    """Lists all todo items."""
    if not todos:
        print("No todos yet.")
    else:
        for i, todo in enumerate(todos):
            print(f"{i + 1}. {todo}")

def complete_todo():
    """Marks a todo item as complete."""
    list_todos()
    if not todos:
        return
    try:
        choice = int(input("Enter the number of the todo to complete: "))
        if 1 <= choice <= len(todos):
            todos[choice - 1].completed = True
            print("Todo marked as complete.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_todo():
    """Deletes a todo item."""
    list_todos()
    if not todos:
        return
    try:
        choice = int(input("Enter the number of the todo to delete: "))
        if 1 <= choice <= len(todos):
            todos.pop(choice - 1)
            print("Todo deleted successfully.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to run the todo application."""
    while True:
        print("\n--- ToDo Menu ---")
        print("1. Add todo")
        print("2. List todos")
        print("3. Complete todo")
        print("4. Delete todo")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_todo()
        elif choice == '2':
            list_todos()
        elif choice == '3':
            complete_todo()
        elif choice == '4':
            delete_todo()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
