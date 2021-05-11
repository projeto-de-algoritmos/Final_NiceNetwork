from django.urls import path

from .views import *

urlpatterns = [
    path('followed/', listfollowed),
    path('following/', listfollowing),
    path('recom', listrecommendations),
    path('user', getUser),
    path('search', searchUser)
]