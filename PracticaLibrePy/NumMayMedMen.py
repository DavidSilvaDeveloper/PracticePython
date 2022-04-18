# Realiza un programa que reciba 3 numero e indique cual de ellos es el mayor el menor y el de en medio

n1 = int(input("Ingresa el numero A: "))
n2 = int(input("Ingresa el numero B: "))
n3 = int(input("Ingresa el numero C: "))

if (n1>n2):
  if (n1>n3):
      print("El numero mayor es: "+str(n1))
      if (n2>n3):
        print("El numero medio es: "+str(n2))
        print("El numero menor es: "+str(n3))
      else:
        print("El numero medio es: "+str(n3))
        print("El numero menor es: "+str(n2))
  else:
    print ("El numero mayor es: "+str(n3))
    print ("El numero medio es: "+str(n1))
    print ("El numero menor es: "+str(n2))
else:
  if (n2>n3):
    print ("El numero mayor es: "+str(n2))
    if (n1>n3):
      print ("El numero medio es: "+str(n1))
      print ("El numero menor es: "+str(n3))
    else:
      print ("El numero medio es: "+str(n3))
      print ("El numero menor es: "+str(n1))
  else:
    print ("El numero mayor es: "+str(n3))
    print ("El numero medio es: "+str(n1))
    print ("El numero menor es: "+str(n2))
