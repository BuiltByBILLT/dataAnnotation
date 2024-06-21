import unittest
from datetime import datetime, timedelta
from todo import Task, AdvancedToDoList  # Replace your_module 

class AdvancedToDoListTest(unittest.TestCase):

    def test_add_task(self):
        todo_list = AdvancedToDoList()
        task = Task("Test task", datetime(2024, 3, 15), priority='high', recurring=False)
        todo_list.add_task(task)
        self.assertIn(task, todo_list.tasks)

    def test_add_task_invalid_date(self):
        todo_list = AdvancedToDoList()
        with self.assertRaises(ValueError):
            todo_list.add_task(Task("Invalid task", "not a date", priority='low'))

    def test_add_task_invalid_priority(self):
        todo_list = AdvancedToDoList()
        with self.assertRaises(ValueError):
            todo_list.add_task(Task("Invalid task", datetime(2024, 3, 15), priority='invalid'))

    def test_complete_task(self):
        todo_list = AdvancedToDoList()
        task = Task("Test task", datetime(2024, 3, 15))
        todo_list.add_task(task)
        todo_list.complete_task("Test task")
        self.assertTrue(task.completed)

    def test_complete_task_recurring(self):
        todo_list = AdvancedToDoList()
        task = Task("Recurring task", datetime(2024, 3, 15), recurring=True)
        todo_list.add_task(task)
        original_due_date = task.due_date
        todo_list.complete_task("Recurring task")
        self.assertFalse(task.completed)  # Should be marked incomplete for recurring tasks
        self.assertEqual(task.due_date, original_due_date + timedelta(days=7))

    def test_complete_task_not_found(self):
        todo_list = AdvancedToDoList()
        with self.assertRaises(ValueError) as context:
            todo_list.complete_task("Nonexistent task")
        self.assertEqual(str(context.exception), "Task 'Nonexistent task' not found.")

    def test_reschedule_task(self):
        todo_list = AdvancedToDoList()
        task = Task("Test task", datetime(2024, 3, 15))
        todo_list.add_task(task)
        new_due_date = datetime(2024, 3, 20)
        todo_list.reschedule_task("Test task", new_due_date)
        self.assertEqual(task.due_date, new_due_date)

    def test_reschedule_task_not_found(self):
        todo_list = AdvancedToDoList()
        with self.assertRaises(ValueError) as context:
            todo_list.reschedule_task("Nonexistent task", datetime(2024, 3, 20))
        self.assertEqual(str(context.exception), "Task 'Nonexistent task' not found.")

    def test_get_tasks_by_priority(self):
        todo_list = AdvancedToDoList()
        todo_list.add_task(Task("High priority task", priority='high'))
        todo_list.add_task(Task("Low priority task", priority='low'))
        todo_list.add_task(Task("Normal priority task", priority='normal'))

        high_priority_tasks = todo_list.get_tasks_by_priority('high')
        self.assertEqual(len(high_priority_tasks), 1)
        self.assertEqual(high_priority_tasks[0].name, "High priority task")

    def test_get_overdue_tasks(self):
        todo_list = AdvancedToDoList()
        today = datetime.now().date()
        todo_list.add_task(Task("Overdue task", today - timedelta(days=1)))
        todo_list.add_task(Task("Due today task", today))
        todo_list.add_task(Task("Future task", today + timedelta(days=1)))

        overdue_tasks = todo_list.get_overdue_tasks()
        self.assertEqual(len(overdue_tasks), 1)
        self.assertEqual(overdue_tasks[0].name, "Overdue task")

if __name__ == '__main__':
    unittest.main()