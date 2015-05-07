import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Activity, Task


class ActivityMethodTests(TestCase):
    """
    Activity is the abstract model for Task and Subtask.
    Using Task objects to test Activity.
    """

    def test_is_on_time_with_finished_task(self):
        task = Task(is_finished = True)
        self.assertEqual(task.is_on_time(), None)

    def test_is_on_time_with_future_due_date(self):
        future_date = timezone.now() + datetime.timedelta(days = 30)
        task = Task(due_date = future_date)
        self.assertEqual(task.is_on_time(), True)

    def test_is_on_time_with_past_due_date(self):
        past_date = timezone.now() - datetime.timedelta(days = 30)
        task = Task(due_date = past_date)
        self.assertEqual(task.is_on_time(), False)