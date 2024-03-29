# -*- coding: utf-8 -*-
#

from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from . import api

app_name = "users"

router = DefaultRouter()
router.register(r'users', api.UserViewSet, 'user')

urlpatterns = [
    url(r'^profile/$', api.UserProfileRetrieveApi.as_view(), name='user-profile'),
    path('user/<int:pk>/password', api.UserPasswordChangeApi.as_view()),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
]

urlpatterns += router.urls
