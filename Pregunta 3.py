E = int(input("Ingrese su edad: "))
S = input("Seleccione el sexo: ")
if (S == "M" and E >= 16 and E < 70) or E < 16:
    print("El tipo de vacuna que se debe aplicar es A")
elif S == "F" and E >= 16 and E < 70:
    print("El tipo de vacuna que se debe aplicar es B")
else :
    E > 70
    print("El tipo de vacuna que se debe aplicar es C")
