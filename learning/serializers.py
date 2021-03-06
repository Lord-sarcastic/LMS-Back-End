from rest_framework import serializers
from authentify.models import User

from learning.models.structure import Level, Resource

class LevelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('uuid', 'name', 'description', 'color')


class ResourceSerializer(serializers.ModelSerializer):
    posted_by = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())
    level = serializers.SlugRelatedField(slug_field="name", queryset=Level.objects.all())
    class Meta:
        model = Resource
        exclude = ('id',)
        read_only_fields = ('uuid', 'slug')
