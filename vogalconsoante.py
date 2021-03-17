letra = input('Informe uma letra: ')
faz_parte_do_alfabeto = letra.isalpha()
tamanho_da_entrada = len(letra)

if faz_parte_do_alfabeto and tamanho_da_entrada == 1:
    print('é uma letra!')
    if letra in 'aeiouAEIOU':
        print('é uma vogal')
    else:
        print('é uma consoante')
else:
    print('Não é uma letra')
