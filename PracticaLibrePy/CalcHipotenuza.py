import math

print("Hola y Bienvenido! \n Por favor elige: \n  Opcion #1 para Calcular Hipotenuza \n  Opcion #2 para Salir \n" )

eleccion = int(input("¿1 o 2?: "))

def inicio():    
  if eleccion == 1:
    calcular()
  elif eleccion ==2:
    salir()
  else:
    print("Ingresa una opcion correcta \n")

def calcular ():
    cat1 = float(input(" Ingresa num 1: "))
    cat2 = float(input(" Ingresa num 2: "))
    if cat1>0 and cat2>0:
        hip = math.sqrt(cat1**2 + cat2**2)
        print("\nLa Hipotenuza es: " + str(hip))
    else:
        print("ingresa enteros positivos")

def salir():
  pass

inicio()