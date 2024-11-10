# Define a variável 'tempoExperiencia' com o valor 3, representando anos de experiência
tempoExperiencia = 3
# Verifica se o tempo de experiência é menor que 2
if tempoExperiencia < 2:
# Se a condição for verdadeira (menos de 2 anos), imprime que o nível é júnior
    print('Nível de conhecimento júnior.')
# Verifica se o tempo de experiência está entre 2 e 5 anos (exclusivo para 2 e inclusivo para 5)
elif 2 < tempoExperiencia < 5:
 # Se a condição for verdadeira (entre 2 e 5 anos), imprime que o nível é pleno
    print('Nível de conhecimento pleno.')
else:
# Se nenhuma das condições acima for verdadeira (5 anos ou mais de experiência)
    print('Nível de conhecimento sênior.')
