from django.db import models
from backend.models import TrackObjectStateMixin


def validate_level(level):
    return level % 100 == 0 and level > 0

class Level(TrackObjectStateMixin):
    """
    A level refers to level available in the university or course
    """
    
    name = models.IntegerField(unique=True, validators=[validate_level])
    description = models.TextField(blank=True)
    color = models.CharField(max_length=7, blank=True)