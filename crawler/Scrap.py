#####################################################
#       AGRADECIMENTO AO QUARTO MEMBRO              #
#       PORQUE ELE ESTÁ SEMPRE SALVANDO             #
#           NOSSOS TRABALHOS PRÁTICOS               #
#       E PORQUE TEM UM CORAÇÃO DE MÃE              #
#               É NOIS MANO S2                      #
#####################################################
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import nil as nil
from write_text import escreve, busca

print("Seu dogão tá pedindo o link...\nInforme a ele quantas pacotes (páginas) de links você vai dá-lo:")
max_page = int(input())
max_page += 1
url = "https://www.techtudo.com.br/jogos/reviews.html"
for x in range(1, max_page, 1):
    url = busca(url, x + 1)