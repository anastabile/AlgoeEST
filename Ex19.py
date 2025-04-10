idade=int(input("insira idade"))
atleta=(input("é atleta?"))
genero=(input("insira genero"))
if idade>=15 or idade<=21 and genero=="feminino":
    print("oferecer maquiagem e moda")
elif idade>=22 or idade<=35 and genero=="feminino":
    print("oferecer artigos esportivos e de casa")
elif idade>=15 or idade<=21 and genero=="masculino" and atleta=="nao":
    print("oferecer videogames")
elif idade>=21 or idade<=32 and genero=="masculino" and atleta=="nao":
    print("oferecer jardinagem, livros e eletrodomesticos")
elif idade>=15 or idade<=32 and genero=="masculino" and atleta=="sim":
    print("artigos esportivos")
else:
    print("oferecer artigos infantis")
