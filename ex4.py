# Juliano Visoli Melato | 09/09/2023
# Que exercício do inferno, tá loko
# Nesse exercício eu usei uma mistura de coisas e fui mexendo e atualizando e editando e pesquisando e até perguntei pro chatgpt algumas coisas
# Usamos listas e dicionários nesse exercício, ambos são muito diferentes mas podem ser utilizados em conjunto sem problema
# As listas são estruturas que podem ser ordenadas e atualizadas, podem receber vários itens duplicados e de tipos diferentes
# Os dicionários são ordenados e podem ser atualizados, assim como a lista, porém recebem elementos únicos, ou seja, sem duplicatas

banco_usuarios = {}     # Criação do dicionário global

def cadastrar_usuario():    # Função para o cadastro de usuários
    global banco_usuarios
    nome = input("Digite o nome do usuário: ").lower()
    idade = input("Digite a idade do usuário: ")
    endereco = input("Digite o endereço do usuário: ").lower()
    telefone = input("Digite o telefone do usuário: ")
    
    usuario = {     # Cria um dicionário para armazenar os dados do usuário
        "nome": nome,
        "idade": idade,
        "endereço": endereco,
        "telefone": telefone
    }
    
    while True:     # Solicita campos adicionais e seu respectivo valor em conjunto
        campo = input("Digite um campo adicional ou 'sair' para encerrar: ").lower()
        if campo == 'sair':
            break
        valor = input(f"Digite o valor para o campo '{campo}': ")
        usuario[campo] = valor
    
    banco_usuarios[nome] = usuario      # Armazena o usuário no banco de dados global
    print("Usuário cadastrado com sucesso!")

def imprimir_usuarios(*args):   # Função para imprimir usuários, funciona como um switch case
    global banco_usuarios
    opcao = input("Escolha uma opção:\n1 - Imprimir todos\n2 - Filtrar por nomes\n3 - Filtrar por campos\n4 - Filtrar por nomes e campos\nDigite 'sair' para voltar ao menu principal: ")
    
    if opcao == '1':    # Imprime todos os usuários
        for usuario in banco_usuarios.values():
            print(usuario)
    elif opcao == '2':      # Imprime os usuários com base nos nomes digitados, separados por ", "
        nomes_filtro = input("Digite os nomes dos usuários que deseja filtrar (separados por vírgula e espaço): ").lower().split(', ')
        for nome in args:
            if nome in nomes_filtro:
                print(banco_usuarios[nome])
    elif opcao == '3':      # Imprime todos os usuários com base no valor do campo escolhido
        campo = input("Digite o nome do campo que deseja filtrar: ").lower()
        valor_filtro = input(f"Digite o valor do campo '{campo}' que deseja filtrar: ")
        for nome, usuario in banco_usuarios.items():
            if campo in usuario and usuario[campo] == valor_filtro:
                print(usuario)
    elif opcao == '4':      # Imprime todos os usuários com base nos campos e nomes escolhidos, como se fosse uma junção das opções 2 e 3
        nomes_filtro = input("Digite os nomes dos usuários que deseja filtrar (separados por vírgula e espaço): ").lower().split(', ')
        filtro_campo = input("Digite o nome do campo que deseja filtrar: ").lower()
        filtro_valor = input("Digite o valor que deseja filtrar: ")
        
        for nome, usuario in banco_usuarios.items():
            if nome in nomes_filtro and filtro_campo in usuario and usuario[filtro_campo] == filtro_valor:
                print(usuario)
    elif opcao.lower() == 'sair':
        return
    else:
        print("Opção inválida. Tente novamente.")

def main():     # Função "main" de execução
    print("Bem-vindo ao banco de dados de usuários!")
    
    while True:     # Menu do programa
        print("\nMenu:")
        print("1 - Cadastrar usuário")
        print("2 - Imprimir usuários")
        print("0 - Sair do programa")
        escolha = input("Digite a opção desejada: ")
        
        if escolha == '1':
            cadastrar_usuario()
        elif escolha == '2':
            imprimir_usuarios(*banco_usuarios.keys())
        elif escolha == '0':
            print("Obrigado por usar o banco de dados de usuários. Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
