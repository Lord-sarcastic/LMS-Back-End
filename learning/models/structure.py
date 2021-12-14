from django.db import models
from django.template.defaultfilters import slugify
from authentify.models import User
from backend.models import TrackObjectStateMixin


def validate_level(level):
    return level % 100 == 0 and level > 100

class Level(TrackObjectStateMixin):
    """
    A level refers to level available in the university or course
    """
    
    name = models.IntegerField(unique=True, validators=[validate_level])
    description = models.TextField(blank=True)
    color = models.CharField(max_length=7, blank=True)


    def __str__(self) -> str:
        return str(self.name)


class Resource(TrackObjectStateMixin):
    title = models.CharField(max_length=64)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.FileField(upload_to="resources")
    description = models.TextField()
    slug = models.SlugField(max_length=128, blank=True)
    OWNER_FIELD = 'posted_by'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
