def fibonacci(num):
    serie_F = [0,1]#creo una lista con los dos valores de inicio de fibonacci
    if num == 0: return [0]
    for i in range(num):
        suma = sum(serie_F[-2:])#serie_F[-2:] hace que desde el indice dado -2(anteultimo) hasta :(hasta el final de la lista) sean sumados
        if suma>num: break#si la suma supera el valor dado no agrega el valor a la lista y termina el programa
        serie_F.append(suma)#agrega el valor a la lista
    return serie_F
print(fibonacci(7))
