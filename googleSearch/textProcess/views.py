from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from .Requisicoes import *
from .searches import *


class teste(Requisicao):
    def post(self, request):
        if 'texto' in request.data:
            str_text=request.data['texto']
            #for line in request.data['pesquisa']:
            #    str_text = str_text + line.decode() 
            newText(str_text)
            return Response({'titulo': 'sucesso'})
        str_text=request.data['pesquisa']
        #for line in request.data['pesquisa']:
        #    str_text = str_text + line.decode() 
        print(str_text)
        respo = searchOR(str_text)
        print(respo)
        return Response(respo)

    def get(self, request):
        
        initFiles()
        return Response({'titulo':'BD inicializado','texto':'sucesso meu camarada'})


class uploadText(Requisicao):
     def get(self, request):
        title = request.data['titulo']
        str_text=request.data['texto']
        #for line in request.data['pesquisa']:
        #    str_text = str_text + line.decode() 
        newText(title, str_text)
        initFiles()
        return Response({'titulo': 'sucesso'})

