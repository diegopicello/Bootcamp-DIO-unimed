#enumerate:
carros = ['Gol', 'Celta', 'Palio']
for indice, carro in enumerate(carros):
    print(indice, carro)

#filtro versão 1:
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)#append é uma forma de adicionar novos valores à lista!

#filtro versão 2(mais otimizada):
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]#primeiro "numero" é o retorno: o que vai compor a lista;
#toda a estrutura do "for" é a parte do meio do comprehension;
#apenas a primeira e a segunda parte são obrigatórias, mas para haver um filtro, é preciso de um 'if' (obiviamente)
#última parte é a condição pra saber se o valor deve ser retornado à nova lista!

#modificando valores versão 1:
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)

#modificando valores versão 2:
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]#sem if pois todos os valores da primeira lista serão modificados e mandados para a nova lista