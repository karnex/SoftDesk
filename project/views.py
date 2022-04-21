import re

from django.db.models import Q
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from authentication.permissions import ProjectPermission
from project.models import Project, Contributor
from project.serializers import ProjectSerializer, ProjectDetailSerializer, ContributorSerializer, \
    ContributorAllSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    # permission_classes = [ProjectPermission]

    def get_permissions(self):
        # Vérifier et traiter
        pass

    def get_serializer_class(self):
        return ProjectSerializer if self.action == 'list' or self.action == 'create' else ProjectDetailSerializer

    def get_queryset(self):
        contributors = Contributor.objects.filter(user=self.request.user)
        projects_id = [c.project.id for c in contributors]
        return Project.objects.filter(id__in=projects_id)


class ContributorViewSet(ModelViewSet):
    """ Contributor(s) of a project """
    def get_serializer_class(self):
        return ContributorAllSerializer if self.action == 'list' or self.action == 'create' else ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs['project_pk'])
