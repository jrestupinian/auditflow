from django.urls import path, include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('risktype', views.RiskTypeView)
router.register('risks', views.RiskView)

urlpatterns = [
    path('', include(router.urls)),
]