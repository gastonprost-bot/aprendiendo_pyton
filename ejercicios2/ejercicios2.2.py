def es_primo(num):
    for i in range(2,num-1):#el rango que le doy es a partir de dos(todos son divisibles por 1)y que sea uno menos que el numero (todos son divisibles por si mismos)
        if num%i==0:
            return False
    return True

def primos_hasta(num):
    primos=[]
    for i in range(2,num+1):
        if es_primo(i)==True:
            primos.append(i)
    return primos


print(primos_hasta(37))

