# Faça um programa que leia três números inteiros e no  final mostre qual número é o  maior e o menor entre eles.

numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
numero3 = int(input('Informe o terceiro número: '))

maior = numero1
menor = numero1
if numero2 > maior:
    maior = numero2
if numero2 < menor:
    menor = numero2

if numero3 > maior:
    maior = numero3
if numero3 < menor:
    menor = numero3

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
