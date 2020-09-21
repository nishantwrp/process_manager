import psutil

from .models import *

def get_process_status(task):
    pid = int(task.process_id)
    try:
        process = psutil.Process(pid)

        if process.status() == "zombie":
            return "Killed"

        return (
            "Paused"
            if process.status() == "stopped" else
            "Running")
    except:
        r = TaskAction.objects.filter(task=task, action_type='K')
        return (
            "Killed"
            if r else
            "Finished")
