from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers

User = get_user_model()


class UserListView(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request: HttpRequest) -> HttpResponse:
        users: QuerySet = User.objects.all()
        return Response(serializers.UserListSerializer(users, many=True).data)
