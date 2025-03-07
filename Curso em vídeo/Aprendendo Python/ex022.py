'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas 
O nome com todas minúsculas 
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome.'''

nam = input('Qual o seu nome: ')
first_nam = nam.split()[0]
print('Nome com todas as letras em maiúsculas: {}'.format(nam.upper()))
print('Nome com todas as letras em maiúsculas: {}'.format(nam.lower()))
print('Letras ao todo sem considerar espaços: {}'.format(len(nam.replace(' ', ''))))
print('Número de letras no primeiro nome: {}'.format(len(first_nam)))