# from django.shortcuts import render
from django import http
from django.http import HttpResponse
from django.http.response import HttpResponseBadRequest

from .utils.Graph import Graph
from .utils.sequenceAlignment import sequence_alignment

import json

network = Graph("JOHN")

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
    if not verifyName(name):
        return HttpResponseBadRequest(errors.get("nameError"))

    return HttpResponse(json.dumps(network.reverse_graph().get(name)))

def listrecommendations(request):
    """Retorna uma lista de usuários recomendados para um usuário"""
    network.suggestion_update()
    suggestions = sorted(network.suggestion.items(), 
                            key=lambda value: value[1], 
                            reverse=True)
    recommendations = []
    for sug in suggestions:
        if sug[0] in list(network.graph.get(network.name)):
            continue
        recommendations.append(sug[0])
    return HttpResponse(json.dumps(recommendations[:200]))

def getUser(request, name:str):
    """Retorna informações do usuário"""
    name = name.upper()
    if not verifyName(name):
        return HttpResponseBadRequest(errors.get("nameError"))
    follows = network.graph.get(name)
    reverseGraph = network.reverse_graph_count()
    userStats = {
        "name": name.capitalize(),
        "followingNumber": len(follows),
        "followedNumber": reverseGraph.get(name),
        "followedByCurrentUser": name in network.graph.get(network.name)
    }
    return HttpResponse(json.dumps(userStats))

def setUser(request, name:str):
    """Muda o usuário atual"""
    if not verifyName(name):
        return HttpResponseBadRequest(errors.get("nameError"))
    network.change_user(name.upper())
    return HttpResponse(network.name.capitalize())

def searchUser(request, name):
    """Retorna um usuário com nome semelhante"""
    # TODO implementação temporária
    # name = name.upper()
    # match = []
    # for username in list(network.graph.keys()):
    #     print(name in username)
    #     if name in username:
    #         match.append(username)
    # return HttpResponse(json.dumps(match))
    name = name.upper()
    match = []
    for user in network.graph:
        match.append((user, sequence_alignment(user, name)))
    match.sort(key=lambda x: x[1])
    match = [i for i, _ in match]
    return HttpResponse(json.dumps(match[:200]))

def follow(request, name):
    name = name.upper()
    network.insert_edge(network.name, name)
    return HttpResponse(name)

def unfollow(request, name):
    name = name.upper()
    network.graph[network.name].remove(name)
    return HttpResponse(name)

def getCurrentUser(request):
    return HttpResponse(network.name.capitalize())