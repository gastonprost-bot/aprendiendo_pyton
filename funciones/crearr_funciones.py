#def saludar():
#    print("hola como estas")

#ejecutando la funcion saludar
#saludar()

def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        print(f"hola {nombre} como estas reina")
    else:
        print(f"hola {nombre} como estas flaco")

saludar("martina","mujeR")


def contraseña_ramdom(num):
    chars = "abcdefghij"#tienen que ser al menos 10 valores sino dara problemas 
    num_entero = str(num)#convierte el valor a cadena de texto 
    num = int(num_entero[0])#se queda con el primer valor y convierte la cadena de texto a numero
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num#permite operar con este valor sin mostrarlo en consola

#desempaquetando la funcion
password,numero_utilizado = contraseña_ramdom(98)#como usarmos return al usar la funcion tenemos que ponerle valores a los q se le asignara el resultdo de la funcion

#mostrando los resultados
print(f"tu conntraseña nueva es {password}")
print(f"el numero utilizado para crearla fue {numero_utilizado}")


def primer_numero(num):#retorna el primer numero de cualquier numero ingresado
    lista_de_numeros = "123456789"
    num_entero = str(num)#convierte el valor a cadena de texto 
    primer_valor = int(num_entero[0])#se queda con el primer valor y convierte la cadena de texto a numero
    return primer_valor,num

valor0,numero_completo = primer_numero(523)
print(f"el primer valor de {numero_completo} es {valor0}")

