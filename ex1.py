# Juliano Visoli Melato | 06/09/2023
# Aqui eu não sabia qual estratégia usar, por mais que o professor tenha realizado talvez o código inteiro desse jogo em sala (se não me engano)
# Eu faltei em algumas aulas, eu tive que tentar seguir uma linha de raciocínio e só começar pra ver no que dava
# A parte de listas eu usei apenas na criação do tabuleiro, de resto foi umas manhas que eu vi o pessoal usando na internet
# A estrutura usada nesse exercício foi "lista", basicamente uma lista é um vetor que armazena items diversos onde você pode
# ordenar da maneira que achar melhor e editar da maneira que achar melhor, adicionando items de vários tipos e também os editando e removendo
# Bem legal

def imprimir_tabuleiro(tabuleiro):  # Função SUPER simples pra criação de um tabuleiro
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 15)

def verificar_vitoria(tabuleiro, jogador):  # Verificar linhas, colunas e diagonais pra ver se o jogador venceu
    for i in range(4):
        if all(cell == jogador for cell in tabuleiro[i]):
            return True
        if all(tabuleiro[j][i] == jogador for j in range(4)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(4)) or all(tabuleiro[i][3 - i] == jogador for i in range(4)):
        return True
    return False

def jogo_da_velha():    # O próprio jogo da velha com um laço infinito verificando se alguém venceu ou acabou em empate
    tabuleiro = [[" " for _ in range(4)] for _ in range(4)]
    jogador_atual = "X"
    
    while True:     # Assim como imprimindo o tabuleiro atualizado todo começo de iteração
        imprimir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual}, é sua vez.")
        
        while True:     # Tratativinha de erro bem simples e serena
            try:
                linha = int(input("Digite a linha (0, 1, 2 ou 3): "))
                coluna = int(input("Digite a coluna (0, 1, 2 ou 3): "))
                if 0 <= linha < 4 and 0 <= coluna < 4 and tabuleiro[linha][coluna] == " ":  # Tá feio mas tá funcionando
                    break
                else:
                    print("Movimento inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Use apenas números inteiros.")
        
        tabuleiro[linha][coluna] = jogador_atual
        
        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break
        
        if all(cell != " " for row in tabuleiro for cell in row):   # Verificar empate
            imprimir_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            break
        
        jogador_atual = "O" if jogador_atual == "X" else "X"    # Alternar jogador

if __name__ == "__main__":  # Vi que isso é uma boa prática, ao invés de só chamar a função direto
    jogo_da_velha()
