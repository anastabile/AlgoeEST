
valores=[]
novov=[]
for i in range(1,5):
    valor=int(input("insira valor"))
    valores.append(valor)

add=int(input("insira o numero para multiplicar "))
for valor in valores:
    novov.append(valor*add)
print(f"os valores são {novov}")