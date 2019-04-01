# WEBSCRAPING WIKIPEDIA PAGES WITH PYTHON

# Exemplo montado a partir do exercício de webscraping de Yuri Alexsander

# Teste 2

###

# IMPORTANDO BIBLIOTECAS
import requests
import bs4


# DECLARANDO VARIÁVEIS

#variáveis de apoio - apagar ao terminar
count = 0
test = {}
temp1 = ""
temp2 = []

#variáveis reais
#variaveis soup
ttl = ""
intro = ""
txt = ""

#variaveis/arrays para conter texto
titulo = ""
in_prgrf = []
index = []
sub_ttl = []
prgrf = []


# REQUISIÇÃO DE UMA PÁGINA DA WIKIPEDIA
response = requests.get ("https://en.wikipedia.org/wiki/Ramesses_V")

# CASO A REQUISIÇÃO TENHA SUCESSO
if response.status_code == 200:
    print("Ok.")

    # UTILIZANDO A BIBLIOTECA BEAUTIFUL SOUP PARA ACESSAR O CONTEÚDO DA REQUISIÇÃO
    bsoup = bs4.BeautifulSoup(response.content, "html.parser")


    # BUSCANDO O TÍTULO DO ARTIGO
    ttl = bsoup.find("div", id="content")
    titulo = ttl.find("h1").get_text()


    # INTRODUCAO DO ARTIGO
    txt = bsoup.find("div", attrs={"mw-parser-output"})

    for row in txt:
        #print(row.find("p"))
        if row.name == "p":
            in_prgrf.append(row.get_text())
            #print("ok ---------------")
        elif row.name == "div":
            #print("terminou --------------")
            break


    # INDICE DE SECOES
    ind = bsoup.find("div", id="toc")
    index.append(ind.find("h2").get_text())
    #ind = bsoup.find("ul")  <--- é um problema quando há mais de uma tabela na paǵina

    for row in ind.ul:  # <--- deste jeito é uma navegação dentro da tag anterior ("div", id="toc")
        if row.name == "li":
            index.append(row.find("span", attrs={"class":"toctext"}).get_text())


    # SECOES E PARÁGRAFOS
    for row in txt:
        # este loop cria um dicionário onde o nome do subtitulo é a chave e os parágrafos são os valores
        if row.name == "h2":
            if temp1 != "":
                # entra em ação somente após ter coletado um subtítulo
                # cria uma chave no dicionário (subtitulo) e acrescenta os valores (paragrafos)
                # len(temp1)-6 para remover o "[Edit] no fim do subtitulo
                test[temp1[0:len(temp1)-6]]=temp2
                # apaga a string temp2 para recomeçar a coleta de parágrafos
                temp2 = []

            # salva o subtitulo
            temp1 = row.get_text()

        elif row.name == "p" or row.name == "ul":
            # salva o texto da seção
            temp2.append(row.get_text())

else:
    print("A requisição falhou.")

print(titulo)
print(in_prgrf)
print(index)

for x in range(1,len(index)-1):
    print("\n{}\n{}\n".format(index[x], test[index[x]]))