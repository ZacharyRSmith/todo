import datetime

from django.db import models
from django.utils import timezone


class Activity(models.Model):
    name        = models.CharField(max_length = 40)
    description = models.CharField(max_length = 200)
    due_date    = models.DateTimeField()
    is_finished = models.BooleanField(default = False)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class Task(Activity):
    def is_overdue(self):
        return self.due_date < timezone.now()
    is_overdue.admin_order_field = 'due_date'
    is_overdue.boolean = True

class Subtask(Activity):
    supertask = models.ForeignKey(Task)