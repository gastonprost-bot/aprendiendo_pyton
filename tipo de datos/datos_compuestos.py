#creando una lista con list
#lista = list(["dsgsdg","asfasfas",34534,"gsdds"])

#lista modificable [ ] 
list = ["alto" , 1.83 , "Gaston"]
list[2] = "Gaston Prost"
#print(list[2])

#lista no modificable ( )
tuple = ("alto" , 1.83 , "Gaston")
#tuple[2] = "mariano" ____________esto no se puede hacer
#print(tuple[2])  

#conjunto (set) { } no pueden existir elementos repetidos, no se pueden llamar elementos
set = {"alto" , 1.83 , "Gaston"}

#diccionario = { } en vez de usar un indice ej. [1] usa una palabra ej "altura"
dict = {
    "caracteristica" : "alto",
    "altura" : 1.83,
    "nombre" : "Gaston"
}
print(dict["nombre"])