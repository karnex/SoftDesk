import re

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from authentication.permissions import ProjectPermission
from project.models import Project, Contributor
from project.serializers import ProjectSerializer, ProjectDetailSerializer, ContributorSerializer


class ProjectViewset(ModelViewSet):
    queryset = Project.objects.all()
    # permission_classes = [ProjectPermission]

    def get_serializer_class(self):
        return ProjectSerializer if self.action == 'list' else ProjectDetailSerializer


class ContributorViewset(ModelViewSet):
    serializer_class = ContributorSerializer

    def get_queryset(self):
        project_id = re.search("projects/([0-9]+)/users", self.request.path).group(1)
        return Contributor.objects.filter(project_id=project_id)

