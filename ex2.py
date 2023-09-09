# Juliano Visoli Melato | 06/09/2023
# Aqui eu só reutilizei o outro jogo da velha e adicionei e alterei algumas coisas pra poder encaixar com a dimensão que o usuário escolher
# A estrutura usada aqui foi a lista, pode ser ordenada e atualizada e duplicada à sua escolha

def criar_tabuleiro(dimensao):  # Criei uma função pra fazer o tabuleiro existir com base nas dimensões que o usuário escolher
    tabuleiro = [[" " for _ in range(dimensao)] for _ in range(dimensao)]
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):  # Função SUPER simples pra criação de um tabuleiro
    dimensao = len(tabuleiro)
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * (4 * dimensao - 1))

def verificar_vitoria(tabuleiro, jogador):  # Verificar linhas, colunas e diagonais pra ver se o jogador venceu
    dimensao = len(tabuleiro)
    for i in range(dimensao):
        if all(cell == jogador for cell in tabuleiro[i]):
            return True
        if all(tabuleiro[j][i] == jogador for j in range(dimensao)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(dimensao)) or all(tabuleiro[i][dimensao - 1 - i] == jogador for i in range(dimensao)):
        return True
    return False

def jogo_da_velha():    # O próprio jogo da velha com um laço infinito verificando se alguém venceu ou acabou em empate
    while True:     # Criando o tabuleiro de acordo com o input do usuário
        try:
            dimensao = int(input("Digite a dimensão do tabuleiro (por exemplo, 3 para um tabuleiro 3x3): "))
            if dimensao < 3:
                print("A dimensão do tabuleiro deve ser pelo menos 3.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Use apenas números inteiros maiores ou iguais a 3.")
    
    tabuleiro = criar_tabuleiro(dimensao)
    jogador_atual = "X"
    
    while True:     # Assim como imprimindo o tabuleiro atualizado todo começo de iteração
        imprimir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual}, é sua vez.")
        
        while True:     # Tratativinha de erro bem simples e serena
            try:
                linha = int(input(f"Digite a linha (0-{dimensao - 1}): "))
                coluna = int(input(f"Digite a coluna (0-{dimensao - 1}): "))
                if 0 <= linha < dimensao and 0 <= coluna < dimensao and tabuleiro[linha][coluna] == " ":
                    break
                else:
                    print("Movimento inválido. Tente novamente.")
            except ValueError:
                print(f"Entrada inválida. Use apenas números inteiros entre 0 e {dimensao - 1}.")
        
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
