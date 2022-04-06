from rest_framework.permissions import BasePermission


class ProjectPermission(BasePermission):

    edit_methods = ("GET", "PUT", "PATCH")

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True if request.user.is_authenticated else False
        elif request.method == 'POST':
            return True if request.user.is_authenticated else False
        else:
            print('That method is still not managed: ' + str(request.method))

        return True if request.user.is_authenticated else False
