'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 

O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import choice
num = int(input('Escolha um número entre 0 e 5: '))
list = [0,1,2,3,4,5]
num_escolhido = choice(list)
print('Você acertou!' if num == num_escolhido else 'Errou otário, eu escolhi {}'.format(num_escolhido))

