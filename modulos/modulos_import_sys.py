import sys #permite utilizar sys
#print(sys.path) #me permite ver la ruta actual para luego modificarla
sys.path.append('C:\\Users\\gasto\\OneDrive\\Escritorio\\python\\pruebas')
import pruebas_ramdom
from modulo_saludar import suma
print(pruebas_ramdom.fibonacci(suma(200,33)))

