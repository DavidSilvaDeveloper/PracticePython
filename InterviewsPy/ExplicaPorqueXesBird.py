# Explica porque X es bird y haz ejercicios similares para entender el concepto de scope.

x = "cat"
def f():
  x = "bird"
  def g():
    x = "dog"
    y = "fish"
  print(x)
  g()
f()