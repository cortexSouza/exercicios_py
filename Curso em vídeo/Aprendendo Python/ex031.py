'''
Desenvolva um oprograma que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km, e R$0,45 para viagens mais longas.
'''

km = float(input('Qual a distância em Km da viagem: '))
preço_viagem_curta = km*0.5
preço_viagem_longa = km*0.45
print('Para uma viagem de {:.2f}Km, o valor será de R${:.2f}'.format(km,preço_viagem_curta) if km <= 200 else 'Para viagens de {:.2f}Km, o valor será de R${:.2f}'.format(km,preço_viagem_longa))
