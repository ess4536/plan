from django.shortcuts import render

from .models import Plan, Task
from .serializers import PlanSerializer, TaskSerializer

from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
# Create your views here.

class PlanViewSet(viewsets.ModelViewSet):
    """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.
    """
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = []

class TaskViewSet(viewsets.ModelViewSet):
    """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = []
