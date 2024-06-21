import unittest
from datetime import datetime, timedelta
from todo import Task, AdvancedToDoList  # Replace your_module 

# Here's the AdvancedToDoList and Task class, assuming it's in the same module
# but in practice, you would import the classes from the module where they are defined

class TestAdvancedToDoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = AdvancedToDoList()
        self.now = datetime.now()

    def test_add_task_with_priority(self):
        # Add a high-priority task and check if it's stored properly
        task = Task("High Priority Task", self.now + timedelta(days=2), priority='high')
        self.todo_list.add_task(task)
        self.assertIn(task, self.todo_list.tasks)
        self.assertEqual(len(self.todo_list.get_tasks_by_priority('high')), 1)

    def test_mark_recurring_task_as_completed(self):
        # Add a recurring task, complete it, and ensure it's rescheduled
        recurring_task = Task("Recurring Task", self.now + timedelta(days=1), priority='normal', recurring=True)
        self.todo_list.add_task(recurring_task)
        self.todo_list.complete_task("Recurring Task")
        self.assertFalse(recurring_task.completed)
        self.assertEqual(recurring_task.due_date, self.now + timedelta(days=8))  # Initially 1, then +7

    def test_reschedule_task(self):
        # Add a task, reschedule it, and check the new due date
        task = Task("Reschedulable Task", self.now + timedelta(days=2), priority='normal')
        self.todo_list.add_task(task)
        new_due_date = self.now + timedelta(days=5)
        self.todo_list.reschedule_task("Reschedulable Task", new_due_date)
        self.assertEqual(task.due_date, new_due_date)

    def test_retrieve_tasks_by_priority(self):
        # Add multiple tasks with different priorities and retrieve by priority
        high_task = Task("High Task", self.now + timedelta(days=1), priority='high')
        low_task = Task("Low Task", self.now + timedelta(days=2), priority='low')
        self.todo_list.add_task(high_task)
        self.todo_list.add_task(low_task)
        self.assertEqual(len(self.todo_list.get_tasks_by_priority('high')), 1)
        self.assertEqual(len(self.todo_list.get_tasks_by_priority('low')), 1)

    def test_get_overdue_tasks(self):
        # Add overdue tasks and one that is not overdue, and retrieve overdue tasks
        overdue_task = Task("Overdue Task", self.now - timedelta(days=1), priority='normal')
        not_overdue_task = Task("Not Overdue Task", self.now + timedelta(days=1), priority='normal')
        self.todo_list.add_task(overdue_task)
        self.todo_list.add_task(not_overdue_task)
        overdue_tasks = self.todo_list.get_overdue_tasks()
        self.assertIn(overdue_task, overdue_tasks)
        self.assertNotIn(not_overdue_task, overdue_tasks)

    def test_complete_non_existing_task(self):
        # Try to complete a task that doesn't exist and expect an exception
        with self.assertRaises(ValueError):
            self.todo_list.complete_task("Non-Existing Task")

    def test_reschedule_non_existing_task(self):
        # Try to reschedule a task that doesn't exist and expect an exception
        with self.assertRaises(ValueError):
            self.todo_list.reschedule_task("Non-Existing Task", self.now + timedelta(days=7))

    def test_add_task_with_invalid_date(self):
        # Try to create a task with an invalid due date
        with self.assertRaises(TypeError):
            Task(name="Invalid Date Task", due_date="invalid-date", priority='normal')

    def test_add_task_with_invalid_priority(self):
        # Try to create a task with an invalid priority
        task = Task(name="Invalid Priority Task", due_date=self.now + timedelta(days=1), priority='illegal')
        with self.assertRaises(AssertionError):
            self.assertIn('illegal', ['low', 'normal', 'high'], "Invalid priority set")
        self.todo_list.add_task(task)
        self.assertIn(task, self.todo_list.tasks)
        self.assertEqual(len(self.todo_list.get_tasks_by_priority('illegal')), 0)

if __name__ == '__main__':
    unittest.main()