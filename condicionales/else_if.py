ingreso = 311

gasto_mensual = 50

if ingreso >= 1000:
    if gasto_mensual < 750:
        print("ganas bien en latinoamerica")
    else: 
        print("ganas bien pero gastas mucho")
elif ingreso >= 500:
    print("sos clase media en latinoamerica")

elif ingreso >= 250:
    print("sos clase baja")

else: 
    print("sos pobre")
