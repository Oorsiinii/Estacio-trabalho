# Inicializa a variável 'entrada_idade' como uma string vazia
entrada_idade = str('')
# Inicia um loop infinito que só será interrompido pela instrução 'break'
while True:
 # Solicita ao usuário para digitar um número ou '0' para sair
  # A função input captura a entrada do usuário, strip() remove espaços extras, e str() converte para string
    entrada_idade = str(input('Digite um número qualquer ou 0 para sair: ').strip())
    # Verifica se a entrada do usuário é igual a '0'
    if entrada_idade == '0':
    # Se for igual a '0', imprime a mensagem de encerramento e sai do loop com 'break'
        print("Encerrando o programa...")
        break
    # Se a entrada não for '0', imprime o número digitado pelo usuario
    print(f'Número digitado: {entrada_idade}')
    