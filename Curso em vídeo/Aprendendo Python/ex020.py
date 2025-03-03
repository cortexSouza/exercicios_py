# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
nam1 = input('Nome do aluno: ')
nam2 = input('Nome do aluno: ')
nam3 = input('Nome do aluno: ')
nam4 = input('Nome do aluno: ')
lista = [nam1,nam2,nam3,nam4]
shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))