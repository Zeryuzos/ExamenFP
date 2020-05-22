SM = int(input("Ingrese el salario minimo: "))
P = int(input("Ingrese los puntos del docente: "))
B = 0
if P >= 50 and P <= 100:
    B = 0.10 * SM
elif  P >= 101 and P <= 150:
    B = 0.50 * SM
else :
    B = SM
print (f"El bono total es: {B} soles")