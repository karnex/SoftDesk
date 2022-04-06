from django.db import models

from authentication.models import User
from project.models import Project


class Issue(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    author_user = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    assignee_user = models.ForeignKey(User, related_name='assignee', on_delete=models.CASCADE)
    created_time = models.DateTimeField()


class Comment(models.Model):
    comment_id = models.AutoField(null=False, primary_key=True)
    description = models.CharField(max_length=255)
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField()
