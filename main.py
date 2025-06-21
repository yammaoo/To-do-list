import json
from datetime import datetime

TASKS_FILE = "tasks.json"

class Task:
    def __init__(self, title, due_date=None, category=None, completed=False):
        self.title = title
        self.due_date = due_date  # string in format YYYY-MM-DD
        self.category = category
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "due_date": self.due_date,
            "category": self.category,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data["title"],
            due_date=data.get("due_date"),
            category=data.get("category"),
            completed=data.get("completed", False)
        )

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, due_date=None, category=None):
        self.tasks.append(Task(title, due_date, category))
        print("✅ Task added.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"🗑️ Deleted: {removed.title}")
        else:
            print("❌ Invalid task number.")

    def mark_complete(self, index, complete=True):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = complete
            print(f"{'✔️ Completed' if complete else '❌ Marked incomplete'}: {self.tasks[index].title}")
        else:
            print("❌ Invalid task number.")

    def view_tasks(self, sort_by=None):
        if not self.tasks:
            print("📭 No tasks found.")
            return

        if sort_by == "date":
            self.tasks.sort(key=lambda x: x.due_date or "9999-99-99")
        elif sort_by == "status":
            self.tasks.sort(key=lambda x: x.completed)
        elif sort_by == "category":
            self.tasks.sort(key=lambda x: x.category or "")

        for i, task in enumerate(self.tasks):
            status = "✅" if task.completed else "❌"
            date = task.due_date if task.due_date else "No date"
            cat = f"[{task.category}]" if task.category else ""
            print(f"{i}. {status} {task.title} | Due: {date} {cat}")

    def save_to_file(self):
        with open(TASKS_FILE, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)
        print("💾 Tasks saved.")

    def load_from_file(self):
        try:
            with open(TASKS_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]
                print("📂 Tasks loaded.")
        except FileNotFoundError:
            print("📂 No saved tasks found. Starting fresh.")

def main_menu():
    todo = ToDoList()
    todo.load_from_file()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task complete")
        print("5. Mark task incomplete")
        print("6. Sort tasks")
        print("7. Save tasks")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            todo.view_tasks()
        elif choice == "2":
            try:
                count = int(input("How many tasks would you like to add? "))
                for i in range(count):
                    print(f"\nAdding task {i+1} of {count}")
                    title = input("Task title: ")
                    due_date = input("Due date (YYYY-MM-DD, optional): ").strip() or None
                    category = input("Category (optional): ").strip() or None
                    todo.add_task(title, due_date, category)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "3":
            todo.view_tasks()
            index = int(input("Task number to delete: "))
            todo.delete_task(index)
        elif choice == "4":
            todo.view_tasks()
            index = int(input("Task number to mark complete: "))
            todo.mark_complete(index, True)
        elif choice == "5":
            todo.view_tasks()
            index = int(input("Task number to mark incomplete: "))
            todo.mark_complete(index, False)
        elif choice == "6":
            print("Sort by: date / status / category")
            sort_type = input("Sort type: ")
            todo.view_tasks(sort_by=sort_type)
        elif choice == "7":
            todo.save_to_file()
        elif choice == "0":
            todo.save_to_file()
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()