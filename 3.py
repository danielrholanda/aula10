# 3- Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista = []
for i in range(4):
    x = float (input(f'Digite a {i +1}º nota: '))
    lista.append(x)
print(f'As notas sao:{lista}')   
soma = sum(lista)
media = sum(lista) / len(lista) #soma a lista e acha a quantidade de integrantes na lista
print(f'A media das notas é igual a: {media}')
