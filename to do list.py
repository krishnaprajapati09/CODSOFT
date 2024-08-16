class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def update_task(self, new_description=None, new_due_date=None):
        if new_description:
            self.description = new_description
        if new_due_date:
            self.due_date = new_due_date

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return

        for i, task in enumerate(self.tasks, start=1):
            status = "Done" if task.completed else "Pending"
            print(f"{i}. {task.description} - Due: {task.due_date} [{status}]")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")

    def update_task(self, index, new_description=None, new_due_date=None):
        if 0 <= index < len(self.tasks):
            self.tasks[index].update_task(new_description, new_due_date)
            print("Task updated successfully.")
        else:
            print("Invalid task number.")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task\n2. Update Task\n3. Mark Task Completed\n4. Delete Task\n5. View Tasks\n6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            new_task = Task(description, due_date)
            todo_list.add_task(new_task)
            print("Task added successfully.")
        elif choice == "2":
            todo_list.show_tasks()
            task_num = int(input("Enter the task number to update: ")) - 1
            new_description = input("Enter new task description (leave blank to keep unchanged): ")
            new_due_date = input("Enter new due date (leave blank to keep unchanged): ")
            todo_list.update_task(task_num, new_description if new_description else None, new_due_date if new_due_date else None)
        elif choice == "3":
            todo_list.show_tasks()
            task_num = int(input("Enter the task number to mark as completed: ")) - 1
            todo_list.mark_task_completed(task_num)
        elif choice == "4":
            todo_list.show_tasks()
            task_num = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(task_num)
        elif choice == "5":
            todo_list.show_tasks()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
