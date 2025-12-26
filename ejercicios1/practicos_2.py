tiempo_por_palabra = 0.5 
texto_del_usuario = input("dame cualquier texto real: ")
separando_palabras = texto_del_usuario.split(" ")
cantidad_de_palabras = len(separando_palabras)
tiempo_para_decir_la_frase = cantidad_de_palabras*tiempo_por_palabra

if tiempo_para_decir_la_frase >= 60:
    print(f"para flaco tampoco te pedi un testamento")

print(f"decir esto: ({texto_del_usuario}) te tomaria {tiempo_para_decir_la_frase}seg.")
print(f"dijiste {cantidad_de_palabras} palabras")
print(f"si hablaras un 30% mas rapido tardarias en decir la misma frase {round(tiempo_para_decir_la_frase*0.7,1)}seg.")