from django.db import models

# Create your models here.

class Task(models.Model):
    process_id = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.process_id}'

class TaskAction(models.Model):
    ACTIONS = [
        ('P', 'Pause'),
        ('R', 'Resume'),
        ('S', 'Start'),
        ('K', 'Kill')
    ]

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=1, choices=ACTIONS)
    time = models.DateTimeField()

    def __str__(self):
        return f'{self.task.process_id} - {self.action_type}'
