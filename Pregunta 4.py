V1 = float(input("Ingrese la primera variable: "))
V2 = float(input("Ingrese la segunda variable: "))
S = input("Ingrese la operacion que decea realizar: ")
if S == "+":
    R = V1 + V2
if S == "-":
    R = V1 - V2
if S == "/":
        R = V1 / V2
if S == "*":
    R = V1 * V2
if S == "^":
    R = V1 ^ V2
print("El resultado es; ", R)