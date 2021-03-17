# 7. Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M para matutino,V para vespertino ou N para noturno. 
# No final mostre a mensagem de boas vindas para cada turno. 
# Bom dia, boa tarde, boa noite ou período não encontrado, conforme o caso.
periodo = input('Qual período você estuda, apedeuta? M - matutino, V para vespertino, N - notuno')
if periodo == 'M':
    print('Bom dia, apedeuta!')
elif periodo == 'V':
    print('Boa tarde, apedeuta!')
elif periodo == 'N':
    print('Boa noite, apedeuta!')
else:
    print('Errrrrooooo! (gif do faustão)')
