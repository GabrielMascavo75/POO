'''Escreva uma função que conta a quantidade de vogais em um texto e armazena tal
quantidade em um dicionário, onde a chave é a vogal considerada e o valor é a quantidade
de vezes que essa vogal aparece no texto.
A função deve receber o texto como entrada e retornar o dicionário.
Exemplo:
Para o texto abaixo:
texto = ' faculdade impacta de tecnologia'
A função deve devolver o seguinte dicionário:
{'a': 5, 'u': 1, 'e': 3, 'o' : 2, 'i': 2 }'''

def contar_vogais(texto):
    vogais = "aeiou"
    contagem = {}
    for letra in texto.lower():
        if letra in vogais:
            contagem[letra] = contagem.get(letra, 0) + 1
    return contagem

texto = "faculdade impacta de tecnologia"
print(contar_vogais(texto))
