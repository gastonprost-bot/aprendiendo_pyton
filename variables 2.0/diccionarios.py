#crecreando diccionarios con dict
diccionario = dict(nombre = "gaston",apellido = "prost")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dar","recibir"]): "jajaaj"}

#creando diccionarios con fromkeys 
diccionario = dict.fromkeys(["nombre","apellido"])

#si se crea de esta manera cada letra se usa como clave
diccionario = dict.fromkeys("abcde")

#si se le da un segundo valor luego de hacerlo de esta forma se lo va a asignar a todas las claves
#diccionario = dict.fromkeys("abcde","primeras 5 letras")#por defecto o si no existe un segundo valor el valor es "none"
print(diccionario)