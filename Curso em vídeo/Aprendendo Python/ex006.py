# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número:'))
d = n*2
t = n*3
rq = n**(1/2)
print('O dobro de {} é {}\nO triplo de {} é {}\nA raiz quadrada de {} é {:.2f}'.format(n,d,n,t,n,rq))