#1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = []
for i in range(5):
    x = int (input(f'Digite o {i +1}º numero da lista: '))
    lista.append(x)
print('Lista de numeros',lista)


for i in range(5): # acrescenta novamente o for para dar a posiçao de cada um da lista
    print(f'posição -> {i+1} na lista, tem o conteúdo {lista[i]}')
    