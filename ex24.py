numeros=[]
for i in range (1,6):
    numero=int(input("insira 5 numeros inteiros"))
    numeros.append(numero)

maior=numeros[0]
menor=numeros[1]
    
for numero in numeros:
    if numero>maior:
        maior=numero


print(f"o maior numero é: {maior}")
for numero in numeros:
    if numero<menor:
        menor=numero

print(f"o menor numero é: {menor}")