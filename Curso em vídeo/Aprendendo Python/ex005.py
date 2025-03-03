# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
s = n+1
a = n-1
print('O antecessor de {} é {}\nO sucessor de {} é {}'.format(n,a,n,s))