lista_de_compras = ["casancrem" , "leche" , "salsa de tomate" , 55 , 54 , "carne"]

lista_para_sort = [44 , 55 , False ,  5435  , True]

#len al igual que con las cadenas devuelve la cantidad de elementos en este caso de la lista
cantidad_elementos = len(lista_de_compras)

#agrega elementos a la lista
lista_de_compras.append("zapallo")

#agrega un elemento a la lista con un indice especifico
lista_de_compras.insert(0,"primero")

#agregando otra lista a la lista.(lo agregado debe estar entre corchetes ya q es otra lista)
lista_de_compras.extend(["anteultimo","ultimo"])

#eliminando un elemento de la lista por su indice.(con -1 se puede eliminar el utlimo elemento con -2el anteultimo etc)
lista_de_compras.pop(4)

#remueve un elemnto de la lista por su valor
lista_de_compras.remove("carne")

#elimina todos los elementos de una lista
#lista_de_compras.clear() 

#ordena elementos de una lista(no admite cadenas de texto),el orden es false true y luego los numeros menores a los mayores
lista_para_sort.sort()

#lista_para_sort.sort(reverse=True) invierte el orden en el que sort ordena, por defecto esta en false         sort(reverse=False)

#invierte los elementos de una lista
lista_de_compras.reverse()

#verificando si un elemento esta en la lista. devuelve el indice en el que se encuentra
buscando = lista_de_compras.index("primero")

print(buscando)
print(lista_para_sort)
print(lista_de_compras)


