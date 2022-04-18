# Prueba Técnica Beca Prográmate - PROGRAMA #2 CálculoNotas  

#Soy Hernando Silva, aspirante a beca PROGRÁMATE, estoy resolviendo la prueba técnica, quedo a la espera de la entrevista para explicar cómo solucione este problema y grabe este video mientras estaba contruyecto mi programa.

#LINK DE VIDEO MIENTRAS GENERABA LA CONSTRUCCION DEL PROGRAMA: 
#https://youtu.be/mYRcNICeNXs
#El video esta como OCULTO, es decir solo lo ven quienes tienen el link.

#El siguinte programa resuelve el problema "Realiza un código que lea 3 notas de un alumno, calcula la media e indica el valor de la nota y la palabra "Excelente" si tiene un valor mayor que 8, "Aprobado" entre 5 y 8, "Suspendido" menor a 5. mostrar en pantalla los resultados."

print("¡Hola y Bienvenido al Programa de Computación de Notas!\n")

print("=> INSTRUCCIONES\nEste programa te leerá los datos del estudiante y la cantidad de notas con su respectivo peso y valor; al final te calculará: \nA. El promedio aritmetico. \nB. El ponderado aritmético. \nC. Su valoracion definitiva.\n")

print ("Recuerda que: \n#1. El valor de la nota deberá esta entre 1.0 y 10.0 \n#2. El Peso de la nota es de 1.0 y 5.0\n#3. El ponderado es el promedio tomando en cuenta el peso de las notas.\n#4. El promedio equivale a las notas divididas por la cantidad.\n#5 La valoracion tiene rubrica própia.")

print("Porfavor completa los siguientes datos del estudiante: \n")
import operator

asignatura = input("Asignatura: ")
nombre = input("Nombre: ")
codigo = input("Codigo: ")
cantNotas = int(input("Cantidad de Notas a Calcular: "))

miDiccionario =	{}

for i in range(cantNotas):
  miDiccionario.update({(float(input("\nValor de Nota: "))): (float(input("Peso de Nota: ")))})


def promedioAritmetico():
  promedio= sum(miDiccionario.keys())/cantNotas
  return promedio


def ponderadoAritmetico():
  listaValores = miDiccionario.keys()
  listaPesos = miDiccionario.values()
  listaResul = list(map(operator.mul, listaValores, listaPesos))
  numerador = sum(listaResul)
  promPonderado = numerador / sum(miDiccionario.values())
  return promPonderado


def valoracionDefinitiva():
  valor = promedioAritmetico()
  if valor >= 1  and valor < 5:
    print("La valoracion definitiva es: Suspendido")
  elif valor >= 5  and valor <= 8:
    print("La valoracion definitiva es: Aprobado")
  elif valor > 8  and valor <= 10:
    print("La valoracion definitiva es: Excelente")
  else:
    print("¡Numero fuera de rango!")
  


def resulFinal():
  print("\nEl ponderado según peso es: "+str(ponderadoAritmetico()))
  print("El promedio aritmetico es: "+str(promedioAritmetico()))
  print(valoracionDefinitiva())


resulFinal()


# for i in miDiccionario:
#miDiccionario[] = ))
#miDiccionario[float(input("Peso de Nota: "))] = float(input("\nValor de Nota: "
# miDiccionario({float(input("Peso de Nota: ")):float(input("\nValor de Nota: "))})
#def valoracionDefinitiva():
#sum(miDiccionario.keys())
#pesosNotas = miDiccionario.keys()
#print(pesosNotas)
#valoresNotas = miDiccionario.values()
#print(valoresNotas)
#Jajajajaja el programa funciona siempre y cuando no se ingresen 2 valores iguales porque las claves de los diccionarios solo aceptan valores unicos y reemplazan a los anteriores, jajajaja pero bueno, la solucion es mejorar la estructura con tuplas o listas, toca seguir investigando.
#https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion3/tipo_diccionarios.html
#https://uniwebsidad.com/libros/python/capitulo-8/metodos-de-retorno
#https://1.bp.blogspot.com/-X3Awneh33sE/XKAXYVQmzaI/AAAAAAAAE9Y/o5IUyF3ya9EWNegtO8gJM0pHzAA8pxqlQCLcBGAs/s1600/PROMEDIOS%2BF%25C3%2593RMULAS%2BEJEMPLOS%2BY%2BEXPLICACIONES%2BB%25C3%2581SICAS%2BPDF%2B%25285%2529.gif
#https://es.stackoverflow.com/questions/96261/c%C3%B3mo-puedo-multiplicar-dos-listas
#https://www.mclibre.org/consultar/python/lecciones/python-if-else.html




