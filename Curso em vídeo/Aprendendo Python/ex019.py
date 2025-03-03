# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
nam1 = input('Qual o nome do aluno: ')
nam2 = input('Qual o nome do aluno: ')
nam3 = input('Qual o nome do aluno: ')
nam4 = input('Qual o nome do aluno: ')
list = [nam1,nam2,nam3,nam4]
escolhido = choice(list)
print('O escolhido foi {}'.format(escolhido))