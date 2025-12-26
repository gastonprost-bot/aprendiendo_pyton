del_1_al_10 = [1,2,3,4,5,6,7,8,9,10]


#creando funciones mas sencillamente con lambda
multiplicar_por_2 = lambda x : x*2 #la funcion retorna automaticamente sin necesidad de usar return como en un def
                                #se debe crear con : no con =
print(multiplicar_por_2(5))

#esta funcion hace lo mismo que la de arriba
def MultiplicarX2(num):
    num=num*2
    return num

print(MultiplicarX2(4))

#def es_par(num):
#    if (num%2==0):
#        return(True)

#usando filter con una funcion comun
#numeros_pares = filter(es_par,del_1_al_10)
#print(list(numeros_pares))

#misma funcion que arriba pero mucho mas sencilla
numeros_pares = filter(lambda num:num%2 == 0,del_1_al_10)
print(list(numeros_pares))
