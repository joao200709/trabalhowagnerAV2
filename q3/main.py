# Questão 3: Sistema de autenticação simples
# Usuários e senhas pré-definidos. Criar uma função para autenticar.

usuarios = {
    "admin": "1234",
    "joao": "senha123",
    "maria": "abc@2024"
}

usuario = input("Usuário: ")
senha = input("Senha: ")


def autenticar(usuario, senha):
    if usuarios.get(usuario) == senha:
        print("Autenticação bem-sucedida!")
    else:
        print("Usuário ou senha incorretos.")

autenticar(usuario, senha)