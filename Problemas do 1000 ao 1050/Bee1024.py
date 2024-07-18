def criptografar_linha(linha):
    primeira_passada = []
    for caractere in linha:
        if 'a' <= caractere <= 'z' or 'A' <= caractere <= 'Z':
            primeira_passada.append(chr(ord(caractere) + 3))
        else:
            primeira_passada.append(caractere)
    
    segunda_passada = ''.join(primeira_passada)[::-1]
    
    indice_meio = len(segunda_passada) // 2
    terceira_passada = []
    for i in range(len(segunda_passada)):
        if i >= indice_meio:
            terceira_passada.append(chr(ord(segunda_passada[i]) - 1))
        else:
            terceira_passada.append(segunda_passada[i])
    
    return ''.join(terceira_passada)

import sys
entrada = sys.stdin.read().strip().splitlines()

n = int(entrada[0])  
resultados = []

for i in range(1, n + 1):
    linha = entrada[i]
    linha_criptografada = criptografar_linha(linha)
    resultados.append(linha_criptografada)

for resultado in resultados:
    print(resultado)
