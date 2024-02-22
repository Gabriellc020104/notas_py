aprovados = 0
reprovados = 0

for i in range(1, 21):
    nome = input(f'Digite o nome do {i}º aluno: ')
    matricula = input(f'Digite a matrícula do {i}º aluno: ')
    nota = float(input(f'Digite a nota do {i}º aluno: '))
    
    if nota >= 6:
        aprovados += 1
    else:
        reprovados += 1

print(f'Quantidade de alunos aprovados: {aprovados}')
print(f'Quantidade de alunos reprovados: {reprovados}')