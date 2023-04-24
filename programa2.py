# Construir una función que reciba un valor entero como parámetro y que determine si su último dígito es 4.

print("--------------------------------------")
print("---------EL ULTIMO VALOR ES 4---------")
print("--------------------------------------")

N=int(input("Digite un valor: "))

def Numero_Final_Es_4(N):
    if N % 10 == 4:
        print("El número termina en 4")
        return True
    else:
        print("El número no termina en 4")
        return False
Numero_Final_Es_4(N)
