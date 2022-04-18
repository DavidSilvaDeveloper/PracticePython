from re import A, X


# ==============> CONDICIONALES EJE1
x = 10
def valor_absoluto(x):                              #    Aqui estoy haciendo la buena practica snake, nombrar valores con _ entre ellos
    if x >= 0 :
        valor = x
    else:
        valor = -x
    return valor
print(f'El valor absoluto es: {valor_absoluto(x)}')



# ==============> CONDICIONALES EJE2
z = 15
a = 19
def max_dos_numeros():
    if a > z:
        return a 
    else:
        return z
print(f"El maximo entre los dos es: {max_dos_numeros()}")



# ==============> CONDICIONALES CON OPERADOR TERNARIO
x = -37
def val_absoluto():
    valor = x if x >= 0 else -x
    return valor
val_absoluto()

x = -40
def val_absoluto():
    return x if x >= 0 else -x # Esta forma es aún mas compacta.
val_absoluto()



# ==============> CONDICIONALES SIN OPCION ALTERNATIVA ()
cafe = "Toma tu cafe "
azucar = "Con azucar"
def crear_cafe():
    if cafe + azucar:
        print(cafe + azucar)
    print(cafe)
crear_cafe()

x = 34
def imprimir_numero(x): # Funcion para imprimir numeros con signos.
    if x >= 0.0:
        print("+", end = "")
    print(x)
    return x
imprimir_numero(x)








# TOPIC CONDITIONALS
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
