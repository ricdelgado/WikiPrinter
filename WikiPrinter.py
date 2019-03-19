# WEBSCRAPING WIKIPEDIA PAGES WITH PYTHON

# Exemplo montado a partir do exercício de webscraping de Yuri Alexsander

# Teste 2

###

# IMPORTANDO BIBLIOTECAS
import requests
import bs4


# DECLARANDO VARIÁVEIS
texto = []
titulo = []

# REQUISIÇÃO DE UMA PÁGINA DA WIKIPEDIA
response = requests.get ("https://en.wikipedia.org/wiki/Ramesses_VI")

# CASO A REQUISIÇÃO TENHA SUCESSO
if response.status_code == 200:
    print("Ok.")

    # UTILIZANDO A BIBLIOTECA BEAUTIFUL SOUP PARA ACESSAR O CONTEÚDO DA REQUISIÇÃO
    bsoup = bs4.BeautifulSoup(response.content, "html.parser")

    print(type(bsoup))

    # BUSCANDO O TÍTULO DO ARTIGO
    # A biblioteca bsoup, com a função findAll(), gera variáveis do tipo bs4.element.ResultSet
    # tbsoup é uma variável bs4.element.ResultSet
    tbsoup = bsoup.findAll("h1", attrs={"class": "firstHeading"})

    # TRABALHANDO A STRING DO TÍTULO

    # converter bs4.element.ResultSet em string
    titulo = str(tbsoup)

    # encontrar os índices entre os quais onde o texto alvo está
    m1 = titulo.find('>')
    m2 = titulo.rfind('<')

    # criando um objeto slice, com os índices, para limpar o código html da string
    tSlice1 = slice(m1+1, m2, 1)

    # aplicando o objeto slice na variável
    titulo = titulo[tSlice1]

    # TESTANDO O TÍTUTLO
    print(titulo)


    # Navegando a estrutura para extrair TEXTO
    html = list(bsoup.children)[2]
    head = list(html.children)[1]
    body = list(html.children)[3]
    div1 = list(body.children)[2]
    print(div1)


    '''
    Não é assim que usa:
    tbsoup2 = bsoup.stripped_strings()
    print(tbsoup2)
    print(type(tbsoup2))
    '''

    '''
    Esse aqui extrai todas as strings. Não sei se é possível limpar de algum jeito simples, 
    mas pra uma página da wikipedia, acho que não.
    
    for string in bsoup.strings:
        print(string)
    
    '''

    # Teste extração de texto - funciona, mas talvez n seja o ideal
    # print(bsoup.get_text())

else:
    print("A requisição falhou.")
