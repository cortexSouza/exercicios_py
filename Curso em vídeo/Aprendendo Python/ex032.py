#Ano bissexto
from datetime import date
ano = int(input('Digite o ano (caso queira o ano atual, digite "0"): '))
if ano == 0:
    ano = date.today().year
print('{} é bissexto'.format(ano) if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else '{} não é bissexto'.format(ano))

