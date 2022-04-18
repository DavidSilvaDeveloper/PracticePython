# Prueba Técnica Beca Prográmate - PROGRAMA #1 CálculoCobroEntrada  

#Soy Hernando Silva, aspirante a beca PROGRÁMATE, estoy resolviendo la prueba técnica, quedo a la espera de la entrevista para explicar cómo solucione este problema y grabe este video mientras estaba contruyecto mi programa.

#LINK DE VIDEO MIENTRAS GENERABA LA CONSTRUCCION DEL PROGRAMA: https://youtu.be/c1nti_6IysU
#El video esta como OCULTO, es decir solo lo ven quienes tienen el link.

#El siguinte programa resuelve el problema "Escribe un código para la empresa "GAMES3D" que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada en pantalla. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $8.500 y si es mayor de 18 años, $12.000."

print ("Hola y Bienvenido a nuestra Sala de Juegos Games3D. \n")

nombre = input("Digita tu nombre: ")
tarjetaplay = input("Digita los 9 numeros de tu tarjeta play: ")
print("Tienes un saldo actual de $10.000 COP")
print("\n"+nombre+", ¡Que gusto verte de nuevo!")
saldo = 10000

# Esta funcion muestra el menu principal con 4 opciones
def menuPrincipal():
  intentomP = True
  while intentomP == True:
    opcionElegida = int(input("""\n => MENU PRINCIPAL: \n1. Compra una entrada.\n2. Recarga la tarjeta play.\n3. Revisa las recomendaciones.\n4. ¡Sal a Jugar! \n   Elige un numero del menu para guiarte ---> """))
    if opcionElegida == 1:
      comprarEntrada()
      intentomP = False
    elif opcionElegida == 2:
      recargarTarjeta()
      intentomP = False
    elif opcionElegida == 3:
      recomendaciones()
      intentomP = False
    elif opcionElegida == 4:
      salir()
      intentomP = False
    else:
      print ("\n¡Opcion incorrecta! Por favor elige un numero del menú.\n")


# Esta funcion permite comprar según la edad.
def comprarEntrada():
  intentocE = True
  while intentocE == True:
    edad = int(input("\n Antes de comprar, digita tu edad: "))

    if edad >= 1 and edad < 4:
      print("Genial, tienes "+str(edad)+" años, Toma tu entrada y ¡Entras Gratis! :D")
      menuPrincipal()
      intentocE = False

    elif edad >= 4 and edad <= 18:
      print ("Genial, tienes "+str(edad)+" años, ¡Solo pagas $8500 y entras!")
      banderac1 = True
      while banderac1 == True:
        eleccionCompra = input("¿Quieres comprar, si o no? ---> ")
        if eleccionCompra =="si":
          banderaElco1 = True
          while banderaElco1 == True:
            okoca= input("Digita ok para pagar $8500 ó menu para regresar ---> ")
            if okoca == str("ok"):
              print("¡Compra exitosa!")
              banderaElco1 = False
            elif okoca == str("menu"):
              menuPrincipal()
              banderaElco1 = False
            else:
              print ("¡Error! Digita ok para pagar o menu para regresar")
          print("¡Gracias por tu compra! Toma tu entrada.")
          banderac1 = False
          menuPrincipal()
        elif eleccionCompra == "no":
          menuPrincipal()
          banderac1 = False
        else:
          print ("¡Error! Por favor elige, digitando si ó no.")
      intentocE = False

    elif edad > 18 and edad <= 99:
      print ("Genial, tienes "+str(edad)+" años ¡Solo pagas $12000 y entras!")
      banderac2 = True
      while banderac2 == True:
        eleccionCompra = input("¿Quieres comprar, si o no? ---> ")
        if eleccionCompra =="si":
          banderaElco2 = True
          while banderaElco2 == True:
            okoca= input("Digita ok para pagar $12000 ó menu para regresar ---> ")
            if okoca == str("ok"):
              print("¡Compra exitosa!")
              banderaElco2 = False
            elif okoca == str("menu"):
              menuPrincipal()
              banderaElco2 = False
            else:
              print ("¡Error! Digita ok para pagar o menu para regresar")
          print("¡Gracias por tu compra! Toma tu entrada.")
          menuPrincipal()
          banderac2 = False
        elif eleccionCompra == "no":
          menuPrincipal()
          banderac2 = False
        else:
          print ("¡Error! Por favor elige, digitando si ó no.")
      intentocE = False

    else:
      print ("¡Error! Intenta ingresar tu edad real, o no entrarás.")


# Esta funcion permite recargar la tarjeta.
def recargarTarjeta():
  print("\n=> Menu Recarga")
  print(nombre+", tu tarjeta play es la numero "+tarjetaplay)
  intento = True
  while intento == True:
    recargaElegida = int(input("""1. Recarga $5.000 y te damos $7.000\n2. Recarga $10.000 y de damos $15.000\n3. Recarga $20.000 y te damos $30.000\n4. Volver al menu principal\n Elige un número para RECARGAR ---> """))

    if recargaElegida == 1:
      banderaRe1 = True
      while banderaRe1 == True:
        eleccionRecarga1 = input ("¿Confirmas recarga de $5.000, si o no? ---> ")
        if eleccionRecarga1 == str("si"):
          print("¡Recarga exitosa! Tu saldo es $"+(str(saldo+7000))+" COP")  
          menuPrincipal()
          banderaRe1 = False
        elif eleccionRecarga1 == str("no"):
          menuPrincipal()
          banderaRe1 = False
        else:
          print ("¡Error! Digita si para confirmar o no para regresar al menu")
      intento = False

    elif recargaElegida == 2:
      banderaRe2 = True
      while banderaRe2 == True:
        eleccionRecarga2 = input ("¿Confirmas recarga de $10.000, si o no? ---> ")
        if eleccionRecarga2 == str("si"):
          print("¡Recarga exitosa! Tu saldo es $"+(str(saldo+15000))+" COP")
          menuPrincipal()
          banderaRe2 = False
        elif eleccionRecarga2 == str("no"):
          menuPrincipal()
          banderaRe2 = False
        else:
          print ("¡Error! Digita si para confirmar o no para regresar al menu")
      intento = False

    elif recargaElegida == 3:
      banderaRe3 = True
      while banderaRe3 == True:
        eleccionRecarga3 = input ("¿Confirmas recarga de $20.000, si o no? ---> ")
        if eleccionRecarga3 == str("si"):
          print("¡Recarga exitosa! Tu saldo es $"+(str(saldo+30000))+" COP")
          menuPrincipal()
          banderaRe3 = False
        elif eleccionRecarga3 == str("no"):
          menuPrincipal()
          banderaRe3 = False
        else:
          print ("¡Error! Digita si para confirmar o no para regresar al menu")
      intento = False
      
    elif recargaElegida == 4:
      menuPrincipal()
      intento = False

    else:
      print ("\n ¡Cuidado! Ingresa una edad real, o no entrarás. \n")



def recomendaciones():
  print("\nRecomendaciones: \nTen siempre su entrada, se precavido con los juegos, vigila tus objetos personales, y cerramos a las 9.00pm")
  banderaReco3 = True
  while banderaReco3 == True:
    eleccionRecarga3 = input ("¿Quieres regresar al menu, si o no? ---> ")
    if eleccionRecarga3 == str("si"):
      menuPrincipal()
      banderaReco3 = False
    elif eleccionRecarga3 == str("no"):
      salir()
      banderaReco3 = False
    else:
      print ("¡Error! Digita si para regresar al menu o no para salir")



def salir():
  print("¡Que vuevlas pronto!")
  

menuPrincipal()
