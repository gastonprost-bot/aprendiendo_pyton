este_curso = 1.5
minimo = 2.5
promedio = 4
maximo = 7

crudo_este_curso = 3.5
crudo_promedio = 5

print("A---------------------------------------------------------------------------------------------")
#mostrando diferencias de tiempos

comparacion_minimo = 100-este_curso/minimo*100
comparacion_promedio = 100-este_curso/promedio*100
comparacion_maximo = 100-este_curso/maximo*100

print(f"este curso dura un {round(comparacion_minimo,1)}% menos que el mas rapido")
print(f"este curso dura un {round(comparacion_promedio,1)}% menos que el promedio")
print(f"este curso dura un {round(comparacion_maximo,1)}% menos que el mas lento")

print("B---------------------------------------------------------------------------------------------")
#cuanto crudo remueve 

editado_este_curso = 100-este_curso/crudo_este_curso*100
editado_promedio = 100-promedio/crudo_promedio*100

print(f"remueve un {round(editado_este_curso,1)}% de material inservible")
print(f"remueve un {round(editado_promedio,1)}% de material inservible")

print("C---------------------------------------------------------------------------------------------")

print(f"ver 10 hs de este curso equivalen a {round(10/este_curso*promedio,1)} hs de el promedio de otros cursos")
print(f"ver 10 hs de un curso promedio equivalen a {round(10/promedio*este_curso,1)} hs de este cursos")
