import datetime
from django.core.exceptions import ValidationError
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

    def is_on_time(self):
        if self.is_finished:
            return None

        return self.due_date > timezone.now()
    is_on_time.admin_order_field = 'due_date'
    is_on_time.boolean = True


class Task(Activity):
    pass


class Subtask(Activity):
    supertask = models.ForeignKey(Task)

    def clean(self):
#         supertask.save()
        if self.due_date > self.supertask.due_date:
            raise ValidationError("Subtasks' due date cannot be after their supertasks' due date!")