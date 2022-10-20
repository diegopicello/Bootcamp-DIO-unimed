#.append():
lista = []
lista.append(3)
print(lista)

#.clear(): (limpar a lista)
lista2 = [1, 2, 3, 4]
print(lista2)
lista2.clear()
print(lista2)

#.copy()
lista3 = [1, 2, 3, 4, 5]
listaalterada = lista3.copy()
print(id(lista3), id(listaalterada))

#.extend():
lista3.extend([6, 7, 8])
print(lista3)
