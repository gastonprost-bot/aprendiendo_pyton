cantidad=int(input("cuantos compañeros son "))#pido la cantidad de compañeros y la transformo a entero
compañeros=[]#creo una lista vacia para rellenarla
for i in range(cantidad):#utilizo range para que el loop funcione para la cantidad de chicos que hay
    nombre=input("cual es tu nombre ")#pide nombre
    edad=int(input("cuantos años tienes "))#pide edad y transforma con int la cadena a entero
    datos=(nombre,edad)#crea un par de datos
    compañeros.append(datos)#agrega ese par de datos a COMPAÑEROS
compañeros.sort(key=lambda x:x[1])#ordeno la lista con sort y le pido que la ordene con un key(edad) con lambda le digo que para cada par que se encuentre utilice el que tiene indice 1 (el segundo elemento)
print(compañeros)
asistente=compañeros[0]
profesor=compañeros[-1]
print(f"el profesor es {profesor[0]} y el asistente es {asistente}")

