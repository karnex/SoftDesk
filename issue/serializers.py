from rest_framework import serializers

from issue.models import Issue, Comment


class IssueAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = '__all__'


class CommentAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
