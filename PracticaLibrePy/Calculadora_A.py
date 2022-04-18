print("  \n")

def Operaciones():
  num1 = int(input("Ingresa el primer numero: "))
  num2 = int(input("Ingresa el segundo numero: "))
  simbolo = input("""Ingresa el simbolo para operar: \n + Para Suma  \n - Para Resta \n * Para Multiplicacion \n / Para División \n""")
  if simbolo == "+":
    suma = num1 + num2
    print (("\n Tu suma es: ") + str(suma))
  elif simbolo == "-":
    resta = num1 - num2
    print (("\n Tu resta es: ") + str(resta))
  elif simbolo ==  "*":
    multi = num1 * num2
    print (("\n Tu multiplicacion es: ") + str(multi))
  elif simbolo ==  "/":
    divic = num1 / num2
    print (("\n Tu division es: ") + str(divic))
  else:
    print ("¡WARNING! Por favor Ingresa uno de los simbolos listados")
    Operaciones()

def VolverAoperar():
  intento = True
  while intento == True:
    print("¿Quieres operar de nuevo?" + " y / n \n")
    eleccion = input()
    if eleccion =="y":
      Operaciones()
    elif eleccion == "n":
      intento = False
      print ("\n Muchas Gracias, Que vuelvas Pronto \n")
    else:
      print ("\n ¡WARNING! Por favor elige entre  y / n")

Operaciones()
VolverAoperar()