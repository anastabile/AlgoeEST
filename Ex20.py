idade=int(input("insira idade"))
membro=(input("é membro?"))
acompanhado=(input("esta acomapnhado?"))
if idade>=18 and membro=="sim":
    print("entrada liberada")
elif idade>=18 and membro=="nao" and acompanhado=="nao":
    print("entrada liberada, mas deverá pagar ingresso")
elif idade>=18 and membro=="nao" and acompanhado=="sim":
    print("entrada liberada, mas pagará meia entrada")
else:
    print("entrada não liberada")