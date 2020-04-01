from django.urls import path, include
from . import views

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

# Create your rooting here.
router = routers.DefaultRouter()
router.register('plan', views.PlanViewSet)
router.register('task', views.TaskViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]