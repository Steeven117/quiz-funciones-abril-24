#Construir una función que reciba un valor entero como parámetro y muestra la tabla de multiplicar de dicho valor recibido.
print("--------------------------------------")
print("--------TABLAS DE MULTIPLICAR---------")
print("--------------------------------------")

N = int(input("Ingrese el valor: "))

def tabla_multiplicar(N):
    for i in range(1, 11):
        rta = N*i
        print(N, "x", i, "=", rta)
print(f"La tabla del {N} es:")
tabla_multiplicar(N)