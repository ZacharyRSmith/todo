from django.contrib import admin

from .models import Subtask, Task


class SubtaskInline(admin.TabularInline):
    model = Subtask
    extra = 3
    fk_name = 'supertask'


class TaskAdmin(admin.ModelAdmin):
    fields = ['name', 'due_date', 'description', 'is_finished']
    list_display = ('name', 'description', 'due_date', 'is_on_time', 'is_finished')
    list_filter = ['due_date', 'is_finished']
    inlines = [SubtaskInline]


# class SubtaskAdmin(TaskAdmin):
#     fields = ['name', 'due_date', 'description', 'is_finished', 'supertask']


admin.site.register(Task, TaskAdmin)
# admin.site.register(Subtask, SubtaskAdmin)