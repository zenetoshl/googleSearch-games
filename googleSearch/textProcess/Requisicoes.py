from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from tastypie.authentication import ApiKeyAuthentication

from .Respostas import *

class Requisicao(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        authentication = ApiKeyAuthentication()
        if authentication.is_authenticated(request) is not True:
            return Response(Respostas.NAO_AUTORIZADO.value)

class UploadText(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        authentication = ApiKeyAuthentication()
        if authentication.is_authenticated(request) is not True:
            return Response(Respostas.NAO_AUTORIZADO.value)



class RequisicaoAlterar(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        authentication = ApiKeyAuthentication()
        if authentication.is_authenticated(request) is not True:
            return Response(Respostas.NAO_AUTORIZADO.value)