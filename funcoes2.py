# Define a função 'loginUsuario' que recebe um parâmetro chamado 'perfil'
def loginUsuario(perfil):
 # Verifica se o perfil do usuário, convertido para letras minúsculas, é igual a 'admin'
    if perfil.lower() == 'admin':
 # Se o perfil for 'admin', exibe a mensagem de boas-vindas para o administrador
        print('Bem-vindo, Administrador')
# Se o perfil não for 'admin', exibe a mensagem de boas-vindas para um usuário comum
    else:print('Bem-vindo, Usuário')
# Chama a função 'loginUsuario' passando diferentes valores para o parâmetro 'perfil'
loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')

