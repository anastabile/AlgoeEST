nota1 = float(input("insira nota 1"))
nota2 = float(input("insira nota 2"))
nota3 = float(input("insira nota 3"))
media = (nota1 + nota2 + nota3)/3

if media>=7:
    print ("aprovado")
elif media<7 and media>=5:
    print ("recuperação")
else:
    print ("reprovado")
