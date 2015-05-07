from django.db import models


class Task(models.Model):
    name        = models.CharField(max_length = 40)
    description = models.CharField(max_length = 200)
    due_date    = models.DateTimeField()
    is_finished = models.BooleanField(default = False)


class Subtask(Task):
    supertask = models.ForeignKey(Task, related_name = 'supertask')