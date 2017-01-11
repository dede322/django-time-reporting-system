from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from trs.models import Project, Task
from trs.serializers import ProjectSerializer, TaskSerializer


class ProjectsViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    @detail_route(methods=['get'])
    def tasks(self, request, pk=None):
        tasks = self.queryset.get(pk=pk).tasks.all()
        return Response(TaskSerializer(tasks, many=True).data)


class TasksViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
