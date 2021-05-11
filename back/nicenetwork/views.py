# from django.shortcuts import render
from django.http import HttpResponse

from .utils.Graph import Graph

import json

graph = Graph("WAGNER")

def listfollowing(request):
    return HttpResponse(json.dumps(graph.suggestion))

def listfollowed(request):
    return HttpResponse("ok2")

def listrecommendations(request):
    return HttpResponse("ok3")

def getUser(request):
    return HttpResponse("ok4")

def searchUser(request):
    return HttpResponse("ok5")