from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('awbs', views.AwbView)
router.register('u_tracking_return', views.U_tracking_returnView)

urlpatterns = [
    path('', include(router.urls))
]