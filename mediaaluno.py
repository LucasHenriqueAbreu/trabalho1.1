aluno = input('Informe o nome do aluno')
n1 = input('digite a primeira nota: ')
n2 = input('digite a segunda nota: ')
n3 = input('digite a terceira nota: ')

media = (float(n1) + float(n2) + float(n3)) / 3
if media > 7 or media == 7:
  print(f'{aluno} aprovado com a média: {media}')
else:
  print(f'{aluno} reprovado com a média: {media}')


