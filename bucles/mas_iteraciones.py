numeros = [18,32,44,2]
cadena_de_texto = "este es el texto"

#saltando una parte del bucle con continue
for num in numeros:
    print(f"el numero ahora es es {num}")
    if num == 44:
        continue#todo lo que siga a partir de continue es salteado y pasa a la siguiente vuelta de bucle
    print(f"{num} es diferente de 44")

#deteniendo el bucle con break
for num in numeros:
    print(f"el numero es {num}")
    if num == 32:
        break
    print(num)

#recorriendo cadena de texto(se muestra caracter por caracterer)
for letra in cadena_de_texto:
    print(letra)

#for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)