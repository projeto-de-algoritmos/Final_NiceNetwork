from django.urls import path

from .views import *

urlpatterns = [
    path('followed/', listfollowed),
    path('following/', listfollowing),
    path('recom', listrecommendations),
    path('user/<str:name>', getUser),
    path('search', searchUser),
    path('follow', follow),
    path('unfollow', unfollow),
    path('change/<str:name>', setUser)
]