def frase(nombre,apellido,adjetivo):
    return f"hola {nombre} {apellido}, sos muy {adjetivo}"

frase_final = frase(apellido="prost",adjetivo="burraso",nombre="gaston")#al hacerlo de esta forma no importa el orden en el que esten 

print(frase_final)