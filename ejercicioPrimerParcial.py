print("Bienvenido al Sistema de Secuencias de Coleltz \n")
print("Debes ingresar 7 numeros entre 1 y 258 \n")

prom = 0

for i in range (7):
    num = int(input("Digita el " + str(i+1) + " numero \n"))
    if num <= 0:
         num = int(input("Ingrese el " + str(i+1) + " numero de nuevo dentro del rango permitido (1 - 258) \n"))
    elif num > 258:
         num = int(input("Ingrese el " + str(i+1) + " numero de nuevo dentro del rango permitido (1 - 258) \n"))
    prom += num

prom = int(prom / 7)
print("El numero promedio al que se le hara la secuencia es: "+ str(prom))

while prom != 1:
    if prom%2 == 0:
        print("El numero es par")
        prom = int(prom / 2)
        print(str(prom) + "\n")
    else:
        print("El numero es impar")
        prom = int((prom * 3) + 1)
        print(str(prom) + "\n")
