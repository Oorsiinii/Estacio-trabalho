# Define a variável 'texto' com a string 'Olá, laço for.
texto = 'Olá, laço for.'
# Inicia um loop 'for' que percorre cada caractere em 'texto'
for item in texto:
# Para cada caractere em 'texto', imprime o caractere atual
    print('Caractere: ' + item)
 # Inicia um segundo loop 'for' aninhado que vai de 1 até 10
    for numero in range(1, 11):
 # Para cada valor em 'range(1, 11)', imprime o número do intervalo atual
        print('Número do intervalo: ' + str(numero))
