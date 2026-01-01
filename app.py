class Todo:
    """Represents a single todo item."""
    def __init__(self, name, description=None, status="pending"):
        self.name = name
        self.description = description
        self.status = status

    def __str__(self):
        status_marker = "[X]" if self.status == "complete" else "[ ]"
        description_part = f"\n    {self.description}" if self.description else ""
        return f"{status_marker} {self.name}{description_part}"

todos = []

def add_todo():
    """Adds a new todo item."""
    name = input("Enter the task name: ")
    if not name:
        print("Error: Task name cannot be empty.")
        return
    description = input("Enter the description (optional): ")
    todos.append(Todo(name, description))
    print("Todo added successfully.")

def list_todos():
    """Lists all todo items."""
    if not todos:
        print("No todos yet.")
    else:
        print("\n--- ToDo List ---")
        for i, todo in enumerate(todos):
            print(f"{i + 1}. {todo}")

def update_todo():
    """Updates an existing todo item."""
    list_todos()
    if not todos:
        return
    try:
        choice = int(input("Enter the number of the todo to update: "))
        if 1 <= choice <= len(todos):
            todo = todos[choice - 1]
            new_name = input(f"Enter the new name (current: {todo.name}): ")
            new_description = input(f"Enter the new description (current: {todo.description or 'N/A'}): ")
            if new_name:
                todo.name = new_name
            if new_description:
                todo.description = new_description
            print("Todo updated successfully.")
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

def toggle_status():
    """Toggles the status of a todo item."""
    list_todos()
    if not todos:
        return
    try:
        choice = int(input("Enter the number of the todo to toggle status: "))
        if 1 <= choice <= len(todos):
            todo = todos[choice - 1]
            if todo.status == "pending":
                todo.status = "complete"
            else:
                todo.status = "pending"
            print(f"Todo '{todo.name}' marked as {todo.status}.")
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
        print("3. Update todo")
        print("4. Delete todo")
        print("5. Toggle status")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_todo()
        elif choice == '2':
            list_todos()
        elif choice == '3':
            update_todo()
        elif choice == '4':
            delete_todo()
        elif choice == '5':
            toggle_status()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()