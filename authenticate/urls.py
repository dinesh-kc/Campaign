from django.contrib import admin
from django.urls import path,include
from authenticate import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('register',views.UserViewSet)
router.register('login',views.UserLoginViewset)

urlpatterns = [
  
    path('',include(router.urls)),
]
