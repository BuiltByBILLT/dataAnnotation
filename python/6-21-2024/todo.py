from datetime import datetime, timedelta
class Task:
    def __init__(self, name, due_date=None, priority='normal', recurring=False):
        if not name:
            raise ValueError("Task name cannot be empty.")
        self.name = name
        self.due_date = due_date
        self.completed = False
        self.priority = priority
        self.recurring = recurring

    def mark_completed(self):
        self.completed = True
        if self.recurring:
            self.due_date += timedelta(days=7)  # Assuming weekly recurrence
            self.completed = False

class AdvancedToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.mark_completed()
                return
        raise ValueError(f"Task '{task_name}' not found.")

    def reschedule_task(self, task_name, new_due_date):
        for task in self.tasks:
            if task.name == task_name:
                task.due_date = new_due_date
                return
        raise ValueError(f"Task '{task_name}' not found.")

    def get_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority and not task.completed]

    def get_overdue_tasks(self):
        today = datetime.now().date()
        return [task for task in self.tasks if task.due_date and task.due_date < today and not task.completed]
    
