'''Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro nome e o último nome separadamente. Por exemplo:

Ana Maria de Souza
Primeiro: Ana
Último: Souza
'''

nam_complete = str(input('Digite o seu nome: ')).strip().title()
print(nam_complete.split()[0])
print(nam_complete.split()[-1])