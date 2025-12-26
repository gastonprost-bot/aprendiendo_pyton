#utilizando parametro args
def suma(nombre,*numeros_a_sumar):#no puede haber ninguna otra variable luego de donde usamos el args ya que nunca se ejecutara 
    print(numeros_a_sumar)#como usamos el args ahora esto es una tupla
    return f"{nombre} la suma de los numeros ingresados es {sum(numeros_a_sumar)}"

print(suma("gaston",124,234,46))


def suma2(numeros_a_sumar):
    print(*numeros_a_sumar)#muestra los valores de la lista pero sin la lista
    return sum([*numeros_a_sumar])#como al usar * ya no es una lista ahora lo metemos en una para poder usar sum

print(suma2([125,46,23]))#es necesario pasar una lista si lo hacemos de esta forma