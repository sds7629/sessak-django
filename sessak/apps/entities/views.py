from typing import Any

from rest_framework.views import APIView


class UserList(APIView):  # type:ignore
    def get(self) -> None: ...
