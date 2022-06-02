from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_nested import routers

from authentication.views import AnonymizeViewSet
from issue.views import IssueViewSet, CommentViewSet
from project.views import ProjectViewSet, ContributorViewSet

router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='projects')

project_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
project_router.register(r'issues', IssueViewSet, basename='issues')
project_router.register(r'users', ContributorViewSet, basename='users')

issue_router = routers.NestedSimpleRouter(project_router, r'issues', lookup='issue')
issue_router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('api-auth', include('rest_framework.urls')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/signup/', include('authentication.urls')),
    path('api/anonymize-my-account', AnonymizeViewSet.as_view({'put': 'update'})),
    path('api/token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/', include(project_router.urls)),
    path('api/', include(issue_router.urls))
]
