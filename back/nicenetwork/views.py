# from django.shortcuts import render
from django import http
from django.http import HttpResponse
from django.http.response import HttpResponseBadRequest

from .utils.Graph import Graph

import json

graph = Graph("genildo")

errors = {
    "nameError": "the name must contain only letters",
}

def verifyName(name):
    """Retorna True se o nome apresenta apenas letras"""
    if not name.isalpha():
        return False
    return True

def listfollowing(request):
    #TODO
    return HttpResponse(json.dumps(graph.graph))

def listfollowed(request):
    #TODO
    return HttpResponse("ok2")

def listrecommendations(request):
    # TODO
    return HttpResponse("ok3")

def getUser(request, name:str):
    """Retorna informações do usuário"""
    name = name.upper()
    if not verifyName(name):
        return HttpResponseBadRequest(errors.get("nameError"))
    follows = graph.graph.get(name)
    reverseGraph = graph.reverse_graph()
    userStats = {
        "name": name.capitalize(),
        "followingNumber": len(follows),
        "followedNumber": reverseGraph.get(name),
        "followedByCurrentUser": graph.name in reverseGraph
    }
    return HttpResponse(json.dumps(userStats))

def setUser(request, name:str):
    """Muda o usuário atual"""
    if not verifyName(name):
        return HttpResponseBadRequest(errors.get("nameError"))
    graph.change_user(name.upper())
    return HttpResponse(graph.name.capitalize())
    # user = graph.graph.get(graph.name)
    # return HttpResponse(json.dumps(user))

def searchUser(request):
    # TODO
    return HttpResponse("ok5")

def follow(request):
    # TODO
    return HttpResponse("ok6")

def unfollow(request):
    # TODO
    return HttpResponse("ok7")