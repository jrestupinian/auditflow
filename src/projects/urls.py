from django.urls import path, include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('projects', views.ProjectView)
router.register('tasks', views.Taskview)

urlpatterns = [
    path('', include(router.urls)),

]