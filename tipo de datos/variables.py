#definiendo una variable con camelCase(cada nueva palabra comienza en mayuscula)
nombreCompleto = "Lucas mariano 5"

#definiendo una variable con snake_case 
#nombre_completo = "Lucas mariano"

#concatenar con f-strings (funciona para variables numericas)
bienvenida = f"hola {nombreCompleto} ¿como estas?"

#contatenar con + (solo funciona para cadenas de texto)
#bienvenida = "hola " + nombreCompleto + " ¿como estas?"

print(bienvenida)

#operadores de pertenencia (busca una palabra en la variable)
print("5" in bienvenida) #devuelve true o false en este caso true
print("juan" not in bienvenida) #devuelve true o false en este caso true


