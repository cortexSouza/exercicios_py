n = input('Opa! bão? Digite qualquer coisa ai pra gente ver algumas especificações do que você digitar:')
print('Pelo que pude ver, o que você digitou é:', type(n))
print('Bom, agora veremos outras especs...')
print('o que você digitou é composto só de espaços?', n.isspace())
print('tem números?',n.isnumeric())
print('tem letras?',n.isalpha())
print('É alphanumérico?',n.isalnum())
print('É decimal?',n.isdecimal())
print('tem letras minusculas?',n.islower())
print('tem letras maiúsculas?',n.isupper())