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

def task2home(request):
    return render(request, 'task2home.html')

def allpokemon(request):
    x=requests.get('https://pokeapi.co/api/v2/pokemon?limit=1118')
    pokemon=x.json()    
    output=''
    for i in pokemon["results"]:
        output=output + '<li>' +  i['name'] +'</li>'
    return HttpResponse('<h1>All Pokemon</h1>'+ '<ol>'+ output +'</ol>')

def allabilities(request):
    x=requests.get('https://pokeapi.co/api/v2/ability?limit=327')
    abilities=x.json()    
    output=''
    for i in abilities["results"]:
        output=output + '<li>' +  i['name'] +'</li>'
    return HttpResponse('<h1>All Abilities</h1>'+ '<ol>'+ output +'</ol>')

def allberries(request):
    x=requests.get('https://pokeapi.co/api/v2/berry?limit=64')
    berry=x.json()    
    output=''
    for i in berry["results"]:
        output=output + '<li>' +  i['name'] +'</li>'
    return HttpResponse('<h1>All Berries</h1>'+ '<ol>'+ output +'</ol>')

def task3home(request):
    return render(request, 'task3home.html')

def task3bonus(request):
    return render(request, 'task3bonus.html')

def pokemoninfo(request):
    pokemon=request.GET.get('text')
    x=requests.get('https://pokeapi.co/api/v2/pokemon/'+ pokemon)
    pokemon_dict=x.json() 
    img=pokemon_dict['sprites']['other']['official-artwork']['front_default']
    return render(request, 'pokemoninfo.html',{'list': pokemon_dict, 'pokemon': pokemon, 'img':img}) 
    