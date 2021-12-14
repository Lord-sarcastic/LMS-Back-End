from typing import Optional
from rest_framework import generics, permissions, viewsets
from learning.models.structure import Level, Resource
from learning.permissions import IsOwnerOfResource

from learning.serializers import LevelListSerializer, ResourceSerializer


def parse_to_int(number: str) -> Optional[int]:
    try:
        number = int(number)
    except ValueError:
        number = None
    return number


class LevelListAPIView(generics.ListAPIView):
    """
    Contains list of all levels
    """
    serializer_class = LevelListSerializer
    queryset = Level.objects.all()


class ResourceCreateAPIView(generics.ListCreateAPIView):
    """
    This is to create a resource or to list. You can filter by 
    passing the query parameters:
        - posted_by=[uuid of a user]
        - level=[level the course is assigned to]
    """

    serializer_class = ResourceSerializer

    def get_queryset(self):
        queryset = Resource.objects.all()
        user_uuid = self.request.query_params.get('posted_by')
        level = parse_to_int(self.request.query_params.get('level'))
        if user_uuid is not None:
            queryset = queryset.filter(posted_by__uuid=user_uuid)
        if level is not None:
            queryset = queryset.filter(level__name=level)
        return queryset


class ResourceAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = (IsOwnerOfResource, )
    lookup_field = 'uuid'
