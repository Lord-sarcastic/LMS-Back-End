from django.urls import path, include

from .views import (
    LevelListAPIView,
    ResourceAPIView,
    ResourceCreateAPIView
)

app_name = 'learning'


urlpatterns = [
    path('levels', LevelListAPIView.as_view(), name='level-list'),
    path('resources/', include([
        path('', ResourceCreateAPIView.as_view(), name='resource-create'),
        path("<uuid:uuid>/", ResourceAPIView.as_view(), name="resource")
    ]))
]