from django.urls import path, include
from rest_framework import routers

from project.views import ProjectViewset, ContributorViewset

router = routers.DefaultRouter()
router.register('', ProjectViewset, 'Project')
router.register(r"projects/[0-9]+/users(/[0-9]+)*", ContributorViewset, basename="users")

urlpatterns = [
    path('', include(router.urls)),
]
