from rest_framework import generics
from learning.models.structure import Level

from learning.serializers import LevelListSerializer


class LevelListAPIView(generics.ListAPIView):
    serializer_class = LevelListSerializer
    queryset = Level.objects.all()