nome = input("informe o nome")
idade = (int(input("informe idade")))
turma = (int(input("informe turma")))
print(f"Aluno cadastrado com sucesso: {nome}, {idade} anos, turma {turma}")
if idade>=6:
    print ("matricula realizada com sucesso")
else:
    print ("não foi possível concluir a matrícula: idade menor que 6 anos")