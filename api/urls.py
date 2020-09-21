from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/', AllTasksView.as_view()),
    path('tasks/new/', NewTaskView.as_view()),
    path('tasks/<int:pk>/', TaskStatusView.as_view()),
    path('tasks/<int:pk>/pause/', PauseTaskView.as_view()),
    path('tasks/<int:pk>/resume/', ResumeTaskView.as_view()),
    path('tasks/<int:pk>/kill/', KillTaskView.as_view())
]
