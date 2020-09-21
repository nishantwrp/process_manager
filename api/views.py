from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .serializers import *
from .models import *

class NewTaskView(generics.GenericAPIView):
    """
    Creates a new task (i.e. the sample_process.py).
    """

    authentication_classes = []
    permission_classes = (permissions.AllowAny,)
    serializer_class = TaskSerializer

    def get(self, *args, **kwargs):
        serializer = self.get_serializer()
        response = serializer.create_new_task()
        return Response(response.data, status=status.HTTP_200_OK)

class TaskStatusView(generics.RetrieveAPIView):
    """
    View the detail of a task.
    """

    authentication_classes = []
    permission_classes = (permissions.AllowAny,)
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class AllTasksView(generics.ListAPIView):
    """
    Views the status of all the tasks.
    """

    authentication_classes = []
    permission_classes = (permissions.AllowAny,)
    serializer_class = TaskSummarySerializer
    queryset = Task.objects.all()

class PauseTaskView(generics.GenericAPIView):
    """
    Pauses a task.
    """

    authentication_classes = []
    permission_classes = (permissions.AllowAny,)
    serializer_class = TaskSerializer
    lookup_field = 'pk'
    queryset = Task.objects.all()

    def get_object(self):
        if getattr(self, 'swagger_fake_view', False):
            return None
        return super().get_object()

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
            'task':self.get_object()
        }

    def get(self, *args, **kwargs):
        serailzer = self.get_serializer()
        response = serailzer.pause_task()
        return Response(response.data, status=status.HTTP_200_OK)

class ResumeTaskView(generics.GenericAPIView):
    """
    Resumes a task.
    """

    authentication_classes = []
    permission_classes = (permissions.AllowAny,)
    serializer_class = TaskSerializer
    lookup_field = 'pk'
    queryset = Task.objects.all()

    def get_object(self):
        if getattr(self, 'swagger_fake_view', False):
            return None
        return super().get_object()

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
            'task':self.get_object()
        }

    def get(self, *args, **kwargs):
        serailzer = self.get_serializer()
        response = serailzer.resume_task()
        return Response(response.data, status=status.HTTP_200_OK)

class KillTaskView(generics.GenericAPIView):
    """
    Kills a task.
    """

    authentication_classes = []
    permission_classes = (permissions.AllowAny,)
    serializer_class = TaskSerializer
    lookup_field = 'pk'
    queryset = Task.objects.all()

    def get_object(self):
        if getattr(self, 'swagger_fake_view', False):
            return None
        return super().get_object()

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
            'task':self.get_object()
        }

    def get(self, *args, **kwargs):
        serailzer = self.get_serializer()
        response = serailzer.kill_task()
        return Response(response.data, status=status.HTTP_200_OK)
