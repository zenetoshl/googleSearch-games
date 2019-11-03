from enum import Enum


class Respostas(Enum):
    ERRO = {'status': False}
    NAO_AUTORIZADO = {'status': False, 'detail': "Nao esta autenticado..."}
    SENHA_ERRADA = {'status': False, 'detail': 'Infelizmente a senha nao esta certa. Tenta de novo ai!'}
    USUARIO_NAO_EXISTE = {'status': False, 'detail': 'Esse usuario aparentemente nao existe. Que tal se cadastrar?'}
    ERRO_DESCONHECIDO = {'status': False, 'detail': 'Epa! Esse erro e novo para nos, '
                                                    'vamos dar uma olhada assim que possivel!'}
    REQUISICAO_MAL_FORMATADA = {'status': False, 'detail': 'Infelizmente geramos uma requisicao nao muito bem '
                                                           'feita...'}
    TOKEN_ERRADO = {'status': False, 'detail': 'Houve um problema de autenticacao com os servicos externos...'}
    PESQUISA_NAO_ENCONTRADO = {'status': False, 'detail': "Nao encontramos nenhum resultado para sua pesquisa..."}

    OK = {'status': True}
