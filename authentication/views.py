from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from authentication.models import User
from authentication.serializers import UserSerializer, PasswordSerializer


class SignUpViewset(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        data = {}
        if not request.user.is_superuser:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            if serializer.is_valid():
                try:
                    user = serializer.save()
                except KeyError as ke:
                    data['response'] = f'{ke} is missing !'
                    return Response(data, status=status.HTTP_401_UNAUTHORIZED)
                data['response'] = 'Successfully registered a new user'
                data['email'] = user.email
                data['username'] = user.username
            else:
                data = serializer.errors

            return Response(data)


class AnonymizeViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        user = User.objects.filter(id=self.request.user.id).first()
        if not user:
            return status.HTTP_409_CONFLICT
        user.username = user.first_name = user.last_name = user.email = 'anonymous'
        user.is_active = False
        try:
            user.save()
        except Exception as e:
            raise Exception(e)
        else:
            return Response(status=status.HTTP_200_OK)


class UsersViewset(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
