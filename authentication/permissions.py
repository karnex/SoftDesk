from django.db.models import Q
from rest_framework import permissions

from issue.models import Comment, Issue
from project.models import Project, Contributor

CONTRIB_METHODS = ('POST', 'GET')


class HasProjectPermission(permissions.BasePermission):
    """ Only allow author """
    def has_object_permission(self, request, view, obj):
        # Allow get, head and options request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named 'author'
        return obj.author == request.user


class HasContributorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            project = Project.objects.get(id=view.kwargs['project_pk'])
        except Project.DoesNotExist:
            return False
        else:
            # Project exists, allow GTE, HEAD, OPTIONS if user is contrib or author
            if project in Project.objects.filter(contributors=request.user):
                if request.method in permissions.SAFE_METHODS:
                    return True
            if request.user == project.contributors:
                return True
            return False


class HasIssuePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if Contributor.objects.filter(Q(project=view.kwargs["project_pk"]) & Q(user=request.user)).exists():
            if request.method in CONTRIB_METHODS:
                return True
        if "issue_pk" in view.kwargs:
            issue = Issue.objects.filter(id=view.kwargs["issue_pk"])
            if issue.exists():
                return issue.first().author == request.user
        return False


class HasCommentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if Contributor.objects.filter(Q(project=view.kwargs["project_pk"]) &
                                      Q(project__issues=view.kwargs["issue_pk"])).filter(user=request.user).exists():
            if request.method in CONTRIB_METHODS:
                return True
        if "comment_id" in view.kwargs:
            comment = Comment.objects.filter(id=view.kwargs["comment_pk"])
            if comment.exists():
                return comment.first().author == request.user
        return False
