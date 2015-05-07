# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=200)),
                ('due_date', models.DateTimeField()),
                ('is_finished', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('task_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tasks.Task')),
                ('supertask', models.ForeignKey(related_name='supertask', to='tasks.Task')),
            ],
            bases=('tasks.task',),
        ),
    ]
