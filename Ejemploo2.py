def calcular_OperacionCombinada(a, b, c):
    res = a * b + c
    return res
print("Operaciones Combinadas")
print("Resultado = a * b + c")
def OperacionCombinada():
    numero1 = float(input("Por favor ingrese el valor de 'a': "))
    numero2 = float(input("Por favor ingrese el valor de 'b': "))
    numero3 = float(input("Por favor ingrese el valor de 'c': "))
    resultado = calcular_OperacionCombinada(numero1, numero2, numero3)
    print("El resultado es:", resultado)

OperacionCombinada()
