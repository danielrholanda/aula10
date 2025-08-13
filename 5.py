""" 5- Faça um Programa que leia 5 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores.
"""

vetor = []
vetorpar = []
vetorimpar = []
for i in range(5):
    n = int (input(f'Digite o {i +1}º numero: '))
    vetor.append(n)
    if n % 2 == 0:
        vetorpar.append(n)
     
    else:
         vetorimpar.append(n)  

print(f'Os numeros são:{vetor}')
print(f'Os numeros pares sao{vetorpar}')   
print(f'Os numeros impares sao{vetorimpar}')      