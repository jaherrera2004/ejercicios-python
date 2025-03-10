'''
En una playa de estacionamiento cobran $2.00 por hora o fracción.
Los dias lunes, martes y miercoles, $2.50 los dias jueve y viernes, $3.00 los dias sabados y domingos. Se considera fraccion de hora cuando haya pasado 5 minutos.
Diseñe un programa que determine cuanto debe pagar un cliente por su estacionamiento en un solo dia de la semana. Si el timepo ingresado es incorrecto imprima un mensaje de error
'''

precios = {
    2.0 :["lunes","martes","miercoles"],
    2.5 :["jueves","viernes"],
    3.0 :["sabado","domingo"]
}

dia = input("Ingrese el dia de la semana: ")

try:
    minutos = int(input("Ingrese la cantidad de minutos: "))
except:
    print("Numero incorrecto")
    exit()

if(minutos >= 60*24 or minutos < 0):
    print("Numero incorrecto")
    exit()

horas_facturables = minutos // 60
if(minutos % 60 >= 5):
    horas_facturables += 1


if(dia.lower() in precios[2.0]):
    costo = horas_facturables * 2.0
elif(dia.lower() in precios[2.5]):
    costo = horas_facturables * 2.5
elif(dia.lower() in precios[3.0]):
    costo = horas_facturables * 3.0 
else:
    print("Dia no valido")      
    exit() 

print(f"El costo de estacionamiento es: {costo}")