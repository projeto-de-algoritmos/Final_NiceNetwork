# from django.shortcuts import render
from django import http
from django.http import HttpResponse
from django.http.response import HttpResponseBadRequest

from .utils.Graph import Graph

import json

network = Graph("GENILDO")

errors = {
    "nameError": "the name must contain only letters",
}

def verifyName(name):
    """Retorna True se o nome apresenta apenas letras"""
    if not name.isalpha():
        return False
    return True

def listfollowing(request, name):
    """Retorna os usuários que o usuário segue"""
    if not verifyName(name):
        return HttpResponseBadRequest(errors.get("nameError"))

    return HttpResponse(json.dumps(network.graph.get(name.upper(), [])))

def listfollowed(request, name):
    """Retorna os usuários que seguem o usuário"""
    # if not verifyName(name):
    #     return HttpResponseBadRequest(errors.get("nameError"))
    # name = name.upper()
    # reverseGraph = network.reverse_graph()
    # return HttpResponse(json.dumps(reverseGraph.get(name)))
    return HttpResponse("wait")

def listrecommendations(request):
    """Retorna uma lista de usuários recomendados para um usuário"""
    # recommendations = []
    # for suggestion in network.suggestion:
    #     if network.suggestion.get(suggestion) > 0:
    #         recommendations.append(suggestion)

    # return HttpResponse(json.dumps(network.suggestion))
    return HttpResponse("wait")

def getUser(request, name:str):
    """Retorna informações do usuário"""
    name = name.upper()
    if not verifyName(name):
        return HttpResponseBadRequest(errors.get("nameError"))
    follows = network.graph.get(name)
    reverseGraph = network.reverse_graph()
    userStats = {
        "name": name.capitalize(),
        "followingNumber": len(follows),
        "followedNumber": reverseGraph.get(name),
        "followedByCurrentUser": network.name in reverseGraph
    }
    return HttpResponse(json.dumps(userStats))

def setUser(request, name:str):
    """Muda o usuário atual"""
    if not verifyName(name):
        return HttpResponseBadRequest(errors.get("nameError"))
    network.change_user(name.upper())
    return HttpResponse(network.name.capitalize())
    # user = network.graph.get(network.name)
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