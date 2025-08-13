#2- Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa

lista = []
for i in range(3):
    x = float (input(f'Digite o {i +1}º numero da lista: '))
    lista.append(x)
    lista.reverse() # inverte a lista
print(f'A lista é,{lista}')    


for i in range(3): # acrescenta novamente o for para dar a posiçao de cada um da lista
    print(f'posição -> {i+1} na lista, tem o conteúdo {lista[i]:.0f}')