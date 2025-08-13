# 4-Faça um Programa que leia um vetor de 4 caracteres, 
# e diga quantas consoantes foram lidas. Imprima as consoantes.

vetor = []
total = 0
for i in range(4):
    letra = (input(f'Digite a {i +1}º letra: '))
    vetor.append(letra)
print(f'As letras sao:{vetor}') 

if letra.isalpha() and letra not in 'aeiou':
      total += 1
      print(f'letra {vetor[i]}')
print(f'Foi informado {total} de consoantes')

