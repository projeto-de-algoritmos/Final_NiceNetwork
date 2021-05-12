from django.urls import path

from .views import *

urlpatterns = [
    path('followed/<str:name>', listfollowed),
    path('following/<str:name>', listfollowing),
    path('recom', listrecommendations),
    path('user/<str:name>', getUser),
    path('search/<str:name>', searchUser),
    path('follow/<str:name>', follow),
    path('unfollow/<str:name>', unfollow),
    path('change/<str:name>', setUser),
    path('currentuser', getCurrentUser)
]