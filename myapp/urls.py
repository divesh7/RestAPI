# myapp/urls.py

from django.urls import path, include
from rest_framework import routers
from .views import ClientViewSet, ProjectViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
