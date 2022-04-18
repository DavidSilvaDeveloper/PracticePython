# Realiza un programa que ingrese x cant de numeros (o notas) y me de el promedio de todos.

#Recuerda intentarlo con pseudocodigo para ser lógico.
print("Hola y Bienvenido a promedia numeros. \n\n Porfavor elige: \n  N Para ingresar nota \n  S Para salir \n  CALCULAR Para promediar")

ListaNumeros = []

def inicio():
  eleccion = input("\nEscribe N, S o Calcular: ")
  eleccion_min = eleccion.lower()
  bandera = True
  while bandera == True:
    if eleccion_min == "n":
      ingresar_nota()
      bandera = True
    elif eleccion_min =="calcular":
      promediar()
      bandera = True
    elif eleccion_min =="s":
      salir()
      bandera = True
    else:
      print("Intenta de nuevo eligiendo una opcion correcta ")
      inicio()
      bandera = False

def ingresar_nota():
  habilitador = True
  while habilitador == True:
    NotaIngresada = float(input("Nota: "))

    # Aqui me quede, porque quiero que se pidan LA NOTAS CONSECUTIVAMENTE, luego el ususario ingresa strings, pero dentro de las condicionales, no he podido lograr que se clasifiquen por TIPO DE DATO, si logro hacer que funcione asi, cuando el programa pida la nota el usuario puede escribir la palabra calcular, y continua el programa.
    # La diferencia de este programa con el anterior es que aqui las notas se piden consecutivamente peo en el anterior pregunta la ELECCION antes de metar cada nota. 

    if NotaIngresada is int or float:
      ListaNumeros.append(NotaIngresada)
      habilitador = True
    elif NotaIngresada is str :
      if NotaIngresada is "s" :
        salir()
      elif NotaIngresada == "calcular":
        promediar()
      salir()
    elif NotaIngresada is not int or float:
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


# Asi quiero que funcione.

# Hola y bienvenido a promedia numeros
#   porfavor escribe:
#    N Para ingresar nota
#    S Para salir
#    CALCULAR Para promediar

# Para promediar escribe: P

# Elije : a

# Nota: 5.6
# Nota: 7.8
# Nota: 3.5
# Nota: 3.6
