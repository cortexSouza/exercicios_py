'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas 
O nome com todas minúsculas 
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome.'''

nam_complete = str(input('Qual o seu nome completo?: ')).strip()
print('Seu nome: {}'.format(nam_complete.title()))
print('Nome em maiusculas: {}'.format(nam_complete.upper())) 
print('Nome todas em minusculas: {}'.format(nam_complete.lower()))
print('Numero de letras ao todo: {}'.format(len(nam_complete.replace(' ',''))))
print('Numero de letras no primeiro nome: {}'.format(len(nam_complete.split()[0])))