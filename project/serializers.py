from rest_framework import serializers

from authentication.models import User
from authentication.serializers import UserSimpleSerializer
from project.models import Project, Contributor


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'description']


class ProjectDetailSerializer(serializers.ModelSerializer):

    contributors = UserSimpleSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ContributorAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = '__all__'


class ContributorSerializer(serializers.ModelSerializer):

    user = UserSimpleSerializer()
    project = ProjectSerializer()

    class Meta:
        model = Contributor
        fields = '__all__'
