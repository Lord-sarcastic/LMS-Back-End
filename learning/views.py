from rest_framework import generics, permissions, viewsets
from learning.models.structure import Level, Resource
from learning.permissions import IsOwnerOfResource

from learning.serializers import LevelListSerializer, ResourceSerializer


class LevelListAPIView(generics.ListAPIView):
    """
    Contains list of all levels
    """
    serializer_class = LevelListSerializer
    queryset = Level.objects.all()


class ResourceCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ResourceSerializer
    queryset = Resource.objects.all()

class ResourceAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = (IsOwnerOfResource, )
    lookup_field = 'uuid'
