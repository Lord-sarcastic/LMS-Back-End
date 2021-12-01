from rest_framework import serializers

from learning.models.structure import Level

class LevelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('uuid', 'name', 'description', 'color')