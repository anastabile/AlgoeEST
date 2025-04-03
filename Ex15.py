produto = input("insira nome do produto")
qnt = int(input("insira quantidade comprada"))
valor = int(input("insira valor do produto"))
valorFinal = qnt*valor

if valorFinal>100:
    desconto= valorFinal*0.5
    print (f"O valor com 5% de desconto é: {desconto}")
else:
    print (f"Total: R${valorFinal}")