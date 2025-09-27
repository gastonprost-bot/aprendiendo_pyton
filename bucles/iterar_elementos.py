animales = ["gato","perro","loro","cocodrilo"]

numeros = [18,32,44,2]

vocales = ["a","b","c","d"]

for bicharracos in animales:#bicharracos es un nombre q yo quiera para q se le asigene el valor de la lista
    print(f"ahora la variable es igual a : {bicharracos}")

for sacacuentas in numeros:
    print(f"{sacacuentas} multiplicado por 3 es igual a: {sacacuentas*3}")

for bicharracos,sacacuentas,letra in zip(animales,numeros,vocales):#zip permite iterar varias listas con la misma cantidad de elementos al mismo tiempo
    print(f"este valor es de la lista de animales: {bicharracos}")
    print(f"y este valor es de la lista de numeros: {sacacuentas}")
    print(f"este valor es de la lista de vocales: {letra}")

for canicas in range(0,14):#range muestra todos los elementos desde el primero hasta el ultimo pero no muestra el ultimo(en este caso 14)
   print(canicas)

for num in enumerate(numeros):#num es una tupla por lo tanto se la puede recorrer de esta forma
    print(num)
    print(f"el indice es: {num[0]} y el valor es: {num[1]}")

for num in numeros:
    print(f"ejecutando un bucle, valor actual: {num}")
else:
    print("el bucle termino")


#todo funciona tambien para tuplas y conjuntos(set)
