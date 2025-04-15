
numeros=[]
pares=[]
impares=[]
for i in range(1,9):
    numero=int(input(f"insira valor"))
    numeros.append(numero)

for numero in numeros:
    m=numero % 2
    if m==0:
        par=numero
        pares.append(par)
    else:
        impar=numero
        impares.append(impar)

print(f"{pares} são os pares e {impares} são os impares")