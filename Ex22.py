palavras=[]
palavraMais5=0
for i in range(1,7):
    palavra=(input("insira 6 palavras"))
    palavras.append(palavra)

for palavra in palavras:
    print(len(palavra))

    if len(palavra)>5:
        palavraMais5=palavraMais5+1
    print(f"palavras que tem mais de 5 caracteres?{palavraMais5}")
    print(palavras)