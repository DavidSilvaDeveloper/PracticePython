# Realiza un programa que ingrese x cant de numeros (o notas) y me de el promedio de todos.

#Recuerda intentarlo con pseudocodigo para ser lógico.
print("Hola y Bienvenido a promedia numeros. \n\n Porfavor elige: \n  Opcion a Para ingresar nota \n  Opcion b Para promediar \n  Opcion c Para salir")

ListaNumeros = []

def inicio():
  eleccion = input("\nEleccion A, B o C: ")
  eleccion_min = eleccion.lower()
  bandera = True
  while bandera == True:
    if eleccion_min == "a":
      ingresar_nota()
      bandera = True
    elif eleccion_min =="b":
      promediar()
      bandera = True
    elif eleccion_min =="c":
      salir()
      bandera = True
    else:
      print("Intenta de nuevo eligiendo una opcion correcta ")
      inicio()
      bandera = False

def ingresar_nota():
  habilitador = True
  while habilitador == True:
    NotaIngresada = input("Nota: ")
    if NotaIngresada is int or float:
      ListaNumeros.append(float(NotaIngresada))
      inicio()
      habilitador = True
    elif NotaIngresada is not int or float:
      print("Ingresa un decimal o un entero \n")    
      habilitador = False
    else:
      print("Ingresa un decimal o un entero \n")    
      habilitador = False
  
def promediar():
  total_notas = len(ListaNumeros)
  suma_numeros = sum(ListaNumeros)
  resul_promedio = suma_numeros / total_notas
  print(f"\nEl promedio es: {resul_promedio}")
  inicio()

def salir():
  pass

inicio()

