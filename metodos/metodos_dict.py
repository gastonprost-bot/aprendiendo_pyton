diccionario = {
    "nombre" : "Gaston ",
    "apellido" : "Prost",
    "edad" : 24
}

#devuelve un objeto dict_item y sirve para iterar
claves = diccionario.keys()

#devuelve el valor de la clave, de esta forma si no encuentra la clave no tira error, (devuelve un none si no lo encuentra)
valor = diccionario.get("edad")

#elimina todos los elementos del diccionario
#limpia_diccionario = diccionario.clear()

#elimina un elemento del diccionario
elimina1 = diccionario.pop("edad")

#obtiene un elemento dict_items iterable 
diccionario_iterable = diccionario.items()

print(diccionario_iterable)
