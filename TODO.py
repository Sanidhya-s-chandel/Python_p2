import time
from datetime import datetime

class Task:
    def __init__(self, description, track_time=False):
        self.description = description
        self.completed = False
        self.created_at = datetime.now()
        self.track_time = track_time
        self.start_time = None
        self.end_time = None
    
    def start_task(self):
        if self.track_time:
            self.start_time = time.time()
            print(f"Started task: {self.description} at {datetime.now().strftime('%H:%M:%S')}")
        else:
            print("Time tracking is not enabled for this task.")
    
    def complete_task(self):
        self.completed = True
        if self.track_time and self.start_time:
            self.end_time = time.time()
            elapsed_time = self.end_time - self.start_time
            print(f"Task '{self.description}' completed in {elapsed_time:.2f} seconds.")
        else:
            print(f"Task '{self.description}' marked as completed.")

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{status}] {self.description} (Created: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')})"

class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self):
        description = input("Enter task description: ")
        track_time_input = input("Track time? (yes/no): ").strip().lower()
        track_time = track_time_input == "yes"
        task = Task(description, track_time)
        self.tasks.append(task)
        print(f"Added task: {description}")
    
    def remove_task(self):
        self.list_tasks()
        index = int(input("Enter the index of the task to remove: "))
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Removed task: {removed_task.description}")
        else:
            print("Invalid task index.")
    
    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks):
                print(f"{idx}. {task}")
    
    def complete_task(self):
        self.list_tasks()
        index = int(input("Enter the index of the task to complete: "))
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete_task()
        else:
            print("Invalid task index.")

# Interactive Menu
todo_list = ToDoList()
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Complete Task")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        todo_list.add_task()
    elif choice == "2":
        todo_list.remove_task()
    elif choice == "3":
        todo_list.list_tasks()
    elif choice == "4":
        todo_list.complete_task()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")