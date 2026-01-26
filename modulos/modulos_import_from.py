#utilizando FROM para extraer solo la funcion SUMA 
from modulo_saludar import suma as sumar #AS tambien sirve para renombrar funciones 
#como trajimos esta unica funcion no es necesario la ruta
print(sumar(18,16))
