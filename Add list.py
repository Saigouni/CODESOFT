class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            status = "Done" if task.completed else "Pending"
            print(f"{idx}. {task.description} (Due: {task.due_date}) - {status}")

    def complete_task(self, task_idx):
        if 1 <= task_idx <= len(self.tasks):
            self.tasks[task_idx - 1].completed = True
            print("Task marked as completed!")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Complete Task")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            task = Task(description, due_date)
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.display_tasks()
        elif choice == "3":
            task_idx = int(input("Enter task index to mark as completed: "))
            todo_list.complete_task(task_idx)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
    