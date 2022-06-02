from django.urls import path, include
from rest_framework import routers

from authentication.views import SignUpViewset, AnonymizeViewSet

router = routers.DefaultRouter()
router.register('', SignUpViewset, 'signup')

urlpatterns = [
    path('', include(router.urls)),
]
