import random
a1 = input('Digite um nome: ')
a2 = input('Digite um nome: ')
a3 = input('Digite um nome: ')
a4 = input('Digite um nome: ')
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno sorteado foi o {}'.format(escolhido))
