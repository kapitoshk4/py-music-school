from django.urls import include, path
from rest_framework import routers

from musician.views import MusicianViewSet

router = routers.DefaultRouter()
router.register("musicians", MusicianViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls))
]

app_name = "musician"
