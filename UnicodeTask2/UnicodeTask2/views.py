from django.http import HttpResponse
import requests
import json

def pokemon(request):
    x=requests.get('https://pokeapi.co/api/v2/type')
    poketype=x.json()    #Also can use poketype=json.loads(x.text)
    output=''
    for i in poketype["results"]:
        output=output + ' ' +  i['name'] 
    return HttpResponse('<h1>Pokemon Types</h1>'+ output)