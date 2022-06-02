from django.db import models

from authentication.models import User
from project.models import Project


class Issue(models.Model):
    """ Issue related to a specific project """
    TAG = [('bug', 'bug'), ('task', 'task'), ('improvement', 'improvement')]
    PRIORITY = [('low', 'low'), ('medium', 'medium'), ('high', 'high')]
    STATUS = [('to do', 'to do'), ('in progress', 'in progress'), ('done', 'done')]

    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    tag = models.CharField(max_length=15, choices=TAG)
    priority = models.CharField(max_length=15, choices=PRIORITY)
    project = models.ForeignKey(Project, related_name='issues', on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS)
    author_user = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    assignee_user = models.ForeignKey(User, related_name='assignee', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    """ Comment related to a specific issue """
    description = models.CharField(max_length=255)
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now=True)
