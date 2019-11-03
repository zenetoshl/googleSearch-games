from bs4 import BeautifulSoup
import re
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
import nil as nil

def escreve(link):
    try:
        html = urlopen(link)
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server caiu ou domínio incorreto!")
    else:
        review = BeautifulSoup(html, "html5lib")
        file = open(re.sub(r'[^\w\d\s-]','_', review.title.getText()) + ".txt", 'w')
        tags = review.findAll("", {"class":"corpo-conteudo"})
        if len(tags) == 0:
            tags = review.findAll("p")
        for tag in tags:
            try:
                file.write(tag.getText() + "\n")
            except:
                continue
        file.close()

def busca(link, num_page):
    fim = True
    try:
        html = urlopen(link)
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server caiu ou domínio incorreto!")
    else:
        page = BeautifulSoup(html, "html5lib")
        tags = page.findAll("a")
        for tag in tags:
            try:
                site = tag['href']
            except:
                continue
            else:
                if re.search('\\breview\\b', site, re.IGNORECASE):
                    escreve(str(site))
                if re.search('\\breviews/' + str(num_page) + '.\\b', site, re.IGNORECASE):
                    prox_tag = site
                    fim = False
        if fim:
            return nil
        else:
            return str(prox_tag)