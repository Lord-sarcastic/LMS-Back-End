from django.urls import path
from .views import (
    LevelListAPIView
)

app_name = 'learning'

urlpatterns = [
    path('', LevelListAPIView.as_view(), name='level_list'),
]