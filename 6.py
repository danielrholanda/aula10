"""Faça um Programa que peça as quatro notas de 3 alunos, 
calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0. """
nmaior7 = soma = 0
vetormedia = []
# range 3 é o total de alunos
for i in range(3):
     # faixa de  notas ==>  4  [0,1,2,3]
    for j in range(4):
        nota = float(input(f'Digite a {j+1}º Nota do {i+1}º Aluno'))
        soma = soma + nota
    media = soma/4
    soma = 0
    vetormedia.append(media)

for i in range(3):
    if vetormedia[i] >=7:
        nmaior7 = nmaior7 +1
        #nmaior7 +=1
print(f'A quantidade de alunos que tiveram média maior ou igual a 7 foi {nmaior7}')
