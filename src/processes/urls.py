from django.urls import path, include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('macroprocesses', views.MacroProcessView)
router.register('processes', views.ProcessView)

urlpatterns = [
    path('', include(router.urls)),
]