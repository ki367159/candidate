from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CanVoteMixin:

    @action(['POST'], True, permission_classes=[IsAuthenticated])
    def vote(self, request, pk):
        obj = self.get_object()

        serializer = self.get_serializer(obj)
        return Response(serializer.data)
