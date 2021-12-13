from django.contrib.auth.models import AbstractUser
from django.db import models

from backend.models import TrackObjectStateMixin


class User(AbstractUser, TrackObjectStateMixin):
    pass
