#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

city = str(input('Digite o nome da cidade:')).strip().upper()
print(city.split()[0] == 'SANTO')