import datetime
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.test import TestCase
from .models import Activity, Subtask, Task


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

    def test_str(self):
        task = Task(name = 'Foobar')
        self.assertEqual(str(task), 'Foobar')


def create_task():
    return Task.objects.create(name = "Foo",
                               description = "Foobar",
                               due_date = timezone.now())


class SubtaskMethodTests(TestCase):

    def test_clean_with_bad_due_date(self):
        future_date = timezone.now() + datetime.timedelta(days = 30)
        task = create_task()
        subtask = Subtask(supertask = task, due_date = future_date)
        self.assertRaises(ValidationError, subtask.clean)

    def test_clean_with_good_due_date(self):
        past_date = timezone.now() - datetime.timedelta(days = 30)
        task = create_task()
        subtask = Subtask(supertask = task, due_date = past_date)
        try:
            subtask.clean()
        except ValidationError:
            self.fail("subtask.clean() should not have raised a ValidationError!")