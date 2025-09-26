#creando un conjunto con set
conjunto = set(["dato1","dato2"])

#metiendo un conjunto (set) dentro de otro
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}
print(conjunto2)

#teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#devuelve en boolean si un conjunto es subconjunto del otro (ambos hacen lo mismo)
resultado = conjunto2.issubset(conjunto1) 
resultado = conjunto2 <= conjunto1 

#devuelve en boolean si un conjunto es superconjunto del otro (ambos hacen lo mismo)
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1 #solo mayor no puede ser igual 

#vrifica si los conjuntos comparados no tienen coincidencias, si tienen un elemento en comun devulve false
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)
