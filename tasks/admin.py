from django.contrib import admin

from .models import Subtask, Task


class TaskAdmin(admin.ModelAdmin):
    fields = ['name', 'due_date', 'description', 'is_finished', 'subtasks']
    list_display = ('name', 'description', 'due_date', 'is_overdue', 'is_finished')
    list_filter = ['due_date', 'is_finished']

class SubtaskAdmin(TaskAdmin):
    fields = ['name', 'due_date', 'description', 'is_finished', 'supertask']


admin.site.register(Task, TaskAdmin)
admin.site.register(Subtask, SubtaskAdmin)