""" 7 - Faça um Programa que leia um vetor de 5 números inteiros, 
mostre a soma, a multiplicação e os números.
"""
vetor = []
soma = 0
multiplicacao = 1
for i in range(5):
    n = int (input(f'Digite o {i+1}º Numero'))
    vetor.append(n)
    # soma = soma + n
    soma += n
    multiplicacao *=n
print('Os numeros são...')
for i in range(5):
     print(f'{i+1}º Numero: {vetor[i]}')
print(f'A soma dos numeros são: {soma}')
print(f'A multiplicação dos numeros são: {multiplicacao}')