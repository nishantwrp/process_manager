import subprocess
import datetime

from rest_framework import serializers

from .models import *
from .utils import *

class TaskActionSerializer(serializers.ModelSerializer):
    action = serializers.SerializerMethodField()

    def get_action(self, obj):
        return obj.get_action_type_display()

    class Meta:
        model = TaskAction
        fields = ('time', 'action')

class TaskSerializer(serializers.ModelSerializer):
    actions = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return get_process_status(obj)

    def get_actions(self, obj):
        task_actions = TaskAction.objects.filter(task=obj)
        return TaskActionSerializer(task_actions, many=True).data

    def create_new_task(self):
        process = subprocess.Popen(["python", "sample_process.py"])
        task = Task.objects.create(process_id=process.pid)
        TaskAction.objects.create(task=task, action_type='S', time=datetime.datetime.now())
        return TaskSerializer(task)

    def pause_task(self):
        task = self.context['task']

        if get_process_status(task) != "Running":
            raise serializers.ValidationError("Only a running process can be paused.")

        process = subprocess.Popen(["kill", "-STOP", f'{task.process_id}'])
        process.wait()
        TaskAction.objects.create(task=task, action_type='P', time=datetime.datetime.now())
        return TaskSerializer(task)

    def resume_task(self):
        task = self.context['task']

        if get_process_status(task) != "Paused":
            raise serializers.ValidationError("Only a paused process can be resumed.")

        process = subprocess.Popen(["kill", "-CONT", f'{task.process_id}'])
        process.wait()
        TaskAction.objects.create(task=task, action_type='R', time=datetime.datetime.now())
        return TaskSerializer(task)

    def kill_task(self):
        task = self.context['task']

        if get_process_status(task) == "Killed" or get_process_status(task) == "Finished":
            raise serializers.ValidationError("This process has already finished or was killed.")

        process = subprocess.Popen(["kill", '-KILL', f'{task.process_id}'])
        process.wait()
        TaskAction.objects.create(task=task, action_type='K', time=datetime.datetime.now())
        return TaskSerializer(task)

    class Meta:
        model = Task
        fields = ('id', 'process_id', 'actions', 'status')

class TaskSummarySerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return get_process_status(obj)

    class Meta:
        model = Task
        fields = ('id', 'status')
