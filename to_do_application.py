import json

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        if task and task not in self.tasks:
            self.tasks.append(task)
            print(f"Added task: {task}")
            self.save_tasks()
        elif not task:
            print("Cannot add an empty task.")
        else:
            print(f"Task '{task}' already exists.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Removed task: {task}")
            self.save_tasks()
        else:
            print(f"Task not found: {task}")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print(f"\nTasks ({len(self.tasks)} total):")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def update_task(self, old_task, new_task):
        if old_task in self.tasks:
            if new_task and new_task not in self.tasks:
                self.tasks[self.tasks.index(old_task)] = new_task
                print(f"Updated task: {old_task} → {new_task}")
                self.save_tasks()
            elif not new_task:
                print("Cannot update to an empty task.")
            else:
                print(f"Task '{new_task}' already exists.")
        else:
            print(f"Task not found: {old_task}")

    def clear_tasks(self):
        confirm = input("Are you sure you want to clear all tasks? (yes/no): ")
        if confirm.lower() == "yes":
            self.tasks.clear()
            self.save_tasks()
            print("All tasks have been cleared.")

    def save_tasks(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.tasks, file, indent=4)
            print(f"Tasks saved to {self.filename}")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
            print(f"Tasks loaded from {self.filename}")
        except FileNotFoundError:
            print(f"No saved tasks found in {self.filename}")
        except json.JSONDecodeError:
            print("Error reading tasks file. Resetting tasks.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Update Task")
        print("5. Clear All Tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ").strip()
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ").strip()
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            old_task = input("Enter the task to update: ").strip()
            new_task = input("Enter the new task: ").strip()
            todo_list.update_task(old_task, new_task)
        elif choice == '5':
            todo_list.clear_tasks()
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
