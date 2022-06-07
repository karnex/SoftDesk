from rest_framework.viewsets import ModelViewSet

from authentication.permissions import HasIssuePermission, HasCommentPermission
from issue.models import Issue, Comment
from issue.serializers import IssueAllSerializer, CommentAllSerializer


class IssueViewSet(ModelViewSet):
    """ Issue related to a project """
    permission_classes = [HasIssuePermission]

    def get_serializer_class(self):
        return IssueAllSerializer

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'])

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data['project'] = kwargs['project_pk']
        request.data['author_user'] = request.user.id
        return super(IssueViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data['project'] = kwargs['project_pk']
        request.data['author_user'] = request.user.id
        return super(IssueViewSet, self).update(request, *args, **kwargs)


class CommentViewSet(ModelViewSet):
    """ Comment related to an issue """
    permission_classes = [HasCommentPermission]

    def get_serializer_class(self):
        return CommentAllSerializer

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_pk'])

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data['issue'] = kwargs['issue_pk']
        request.data['author_user'] = request.user.id
        return super(CommentViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data['issue'] = kwargs['issue_pk']
        request.data['author_user'] = request.user.id
        return super(CommentViewSet, self).update(request, *args, **kwargs)
