cadena1 = "no tengo Ni idea"
cadena2 = "53636"

#transforma todo el texto en mayusculas
mayusculas = cadena1.upper()

#transforma todo el texto en minusculas
minusculas = cadena1.lower()

#transforama la primera letra de un texto a mayuscula y el resto lo transforma a minuscula
mayusculas_inicio = cadena1.capitalize()

#busca una cadena en otra.  -1 si no existe
busqueda_fin = cadena1.find("Ni")

#busca una cadena en otra. lanza una exepcion si no existe
busqueda_fin = cadena1.index("Ni")

#comprueba si todo el texto son numeros 
es_numerico = cadena1.isnumeric()

#comprueba si todo el texto son letras (no cuentan como letras caracteres tipo , o espacios)
es_alfanumerico = cadena1.isalnum()

#busca una cadena en otra. devuelve las veces que coincida
cuenta_coincidencia = cadena1.count("n")

#devuelve la cantidad de caracteres de una cadena 
cuenta_caracteres = len(cadena2)

#verifica si empieza con la cadena ingresada
empieza_con = cadena1.startswith("No")

#verifica si termina con la cadena ingresada
termina_con = cadena1.endswith("idea")

#remplaza una parte de una cadena por otra dada
remplazar_en_la_cadena = cadena1.replace("no","si")

#separar cadenas con la cadena que le pasemos y elimina la cadena ingresada 
#ej split("5") en la cadena = 454 devuelve ['4','4']
cadena_separada = cadena1.split("N")

print(cadena_separada)

#print(dir(cadena1)) muestra que funciones le podes aplicar a un dato dir()es una funcion no un metodo


