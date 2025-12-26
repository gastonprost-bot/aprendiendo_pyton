numeros = [12,14,15,643,7,34,12]

#encontrando el valor mas alto de una lista de numeros(solo funciona si todos son numeros)
mas_alto = max(numeros)
print(mas_alto) 

#encontrando el valor mas bajo de una lista de numeros(solo funciona si todos son numeros)
mas_bajo = min(numeros)
print(mas_bajo) 

#redondeando numeros
numero_con_coma = 7/3
print(numero_con_coma)
print(round(numero_con_coma,2))

#retorna false si 0, vacio, false o none/ retorna true si distinto a 0, true, cadena, dato no vacio
resultado_bool = bool(0)
print(resultado_bool)

#retorna treu si todos los valores son verdaderos
resultado_all = all([234,"True",[False]])#el 0 y false dentro de otra lista sigue retornando true
print(resultado_all)

#sunma todos los valores de una lista iterable
suma_total = sum(numeros)
print(suma_total)

