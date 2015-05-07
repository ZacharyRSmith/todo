import datetime

from django.db import models
from django.utils import timezone


class Task(models.Model):
    name        = models.CharField(max_length = 40)
    description = models.CharField(max_length = 200)
    due_date    = models.DateTimeField()
    is_finished = models.BooleanField(default = False)

    def __unicode__(self):
        return self.name

    def is_overdue(self):
        return self.due_date < timezone.now()
    is_overdue.admin_order_field = 'due_date'
    is_overdue.boolean = True

class Subtask(Task):
    supertask = models.ForeignKey(Task, related_name = 'supertask')