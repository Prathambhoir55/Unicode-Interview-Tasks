from django.http import HttpResponse
import requests
from django.shortcuts import render
import json

def index(request):
    return render(request, 'index.html')

def task2(request):
    x=requests.get('https://pokeapi.co/api/v2/type')
    poketype=x.json()    #Also can use poketype=json.loads(x.text)
    output=''
    for i in poketype["results"]:
        output=output + '<li>' +  i['name'] +'</li>'
    return HttpResponse('<h1>Pokemon Types</h1>'+ '<ol>'+ output +'</ol>')

def task3(request):
    return render(request, 'task3.html')

def pokemon(request):
    type=request.GET.get('text')
    x=requests.get('https://pokeapi.co/api/v2/type')
    poketype=x.json() 
    output=''   
    for i in poketype["results"]:
        if type==i['name']:
            k=requests.get(i['url'])
            poketype2=k.json()
            for j in poketype2["pokemon"]:
                output=output + '<li>' + j['pokemon']['name'] + '</li>'
    return HttpResponse('<h1>Pokemon</h1>'+ '<ul>' + output + '</ul>')