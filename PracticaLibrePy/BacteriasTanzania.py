
años = 0

x_hab = 50
y_bac = 40

porcentaje_A = 10
porcentaje_B = 15

while x_hab > y_bac:
  aumento_x = x_hab * (porcentaje_A / 100)
  aumento_y = y_bac * (porcentaje_B / 100)
  x_hab = x_hab + aumento_x
  y_bac = y_bac + aumento_y
  años += 1

print(f" Años para que # bacterias superen a # habitantes {años}")

# Ejercico 26 de Marzo.