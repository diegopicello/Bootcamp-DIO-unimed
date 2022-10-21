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

#.pop():
#"retira o último prato da pilha de pratos" da lista (analogia professor)
#perceba: o append adiciona um elemento no fim da lista e o pop tira o último elemento da lista
linguagens = ['Python', 'JS', 'C', 'Java', 'C#']
linguagens.pop() #c#
linguagens.pop() #java
linguagens.pop() #c
linguagens.pop(0) #python

#.remove():
#Útil para remover um elemento que você já sabe, mas ele só remove a primeira ocorrência! Cuidado com isso!

#.reverse():
#inverte os elementos da lista




