diccionario = {
    "nombre" : "Gaston ",
    "apellido" : "Prost",
    "edad" : 24
}


#de esta forma solo se muestra la key(clave) 
for elemento in diccionario:
    print(elemento)


#recorriendo el diccionario con items() para obterner la clave y el valor
for key in diccionario.items():
    print(f"la clave es {key[0]} y el varor es {key[1]}")

#recorriendo el diccionario con items() para obterner solo el valor
for key in diccionario.items():
    print(f"el varor es {key[1]}")

#otra forma de mostrar el key y el value
for key,value in diccionario.items():
    print(key,value)

