def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No es posible dividir por cero."

# Solicitar al usuario dos números y la operación a realizar
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

operacion = input("Ingrese la operación a realizar (+, -, *, /): ")

# Realizar la operación seleccionada
if operacion == "+":
    resultado = suma(num1, num2)
elif operacion == "-":
    resultado = resta(num1, num2)
elif operacion == "*":
    resultado = multiplicacion(num1, num2)
elif operacion == "/":
    resultado = division(num1, num2)
else:
    resultado = "Operación no válida."

# Mostrar el resultado
print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")

