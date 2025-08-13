# 4-Faça um Programa que leia um vetor de 10 caracteres, 
# e diga quantas consoantes foram lidas. Imprima as consoantes.

vogais = ['a','e','i','o','u']
consoantes = []

for i in range(10):
    v = (input(f'Digite as consoantes: ')).lower() #lower transformar maiusculo/minusculo

    if len(v) == 1 and v.isalpha() and v not in vogais: #len numero de item
     consoantes.append(v) 
     # isalpha - é utilizado para verificar se todos os caracteres em uma string são letras do alfabeto
     # append acrescentar na lista
     
print('----------')

print('A quantidade de consoantes é igual a: ',len(consoantes))
