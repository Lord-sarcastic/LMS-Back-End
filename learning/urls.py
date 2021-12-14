from django.urls import path, include

# from rest_framework import routers

from .views import (
    LevelListAPIView,
    ResourceAPIView,
    ResourceCreateAPIView
)

app_name = 'learning'

# router = routers.DefaultRouter()
# router.register('resources', ResourceAPIView, basename='resources')

urlpatterns = [
    path('', LevelListAPIView.as_view(), name='level_list'),
    path('resources/', include([
        path('', ResourceCreateAPIView.as_view(), name='resource-create'),
        path("<uuid:uuid>/", ResourceAPIView.as_view(), name="resource")
    ]))
]