'''faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A"
Em que posição aparece a primeira vez.
Em que posição parece a última vez. 
'''

frase = str(input('Escreva uma frase: ')).strip().lower()
print(frase.count('a'))
print(frase.find('a')+1)
print(frase.rfind('a')+1)