# Juliano Visoli Melato | 09/09/2023
# Esse exercício eu não fazia a MÍNIMA ideia do que eu tava fazendo, nada funcionava do jeito que eu queria
# e por mais que eu pesquisava muito e ia atrás de muita coisa, no final não ficou muito como o Termo
# usei o chatgpt em algumas partes, principalmente na parte de mostrar as letras e a palavra e a junção de letras e tudo mais
# Na parte de uso de arquivo, na verdade é bem simples, só alterei pra não pegar todas as palavras e sim as que são de 5 letras, como no Termo
# Infelizmente muitas palavras estão com os caracteres especiais e eu pesquisei e não soube como "adicionar" eles por aqui
# então algumas palavras estão com as letras estranhas quando aparecem no terminal, não são todas, mas ainda assim
# Aqui usamos lista como a estrutura principal, boa parte foi criado direto na mão, ao invés de atribuir com as '[]'

import random

def escolher_palavra():     # Função para escolher uma palavra aleatória do arquivo txt
    with open("lista_palavras.txt", "r") as arquivo:
        palavras = arquivo.readlines()
    palavras_com_5_letras = [palavra.strip() for palavra in palavras if len(palavra.strip()) == 5]
    return random.choice(palavras_com_5_letras)

def mostrar_palavra(palavra_secreta, letras_certas, letras_certas_posicao_errada):      # Função para exibir as letras
    resultado = list("_" * len(palavra_secreta))                                        # certas na palavra secreta
                                                                                        # certas mas na posição errada
    for letra, posicao in letras_certas:
        resultado[posicao] = letra
    
    tabela_letras_erradas = list("_" * len(palavra_secreta))
    for letra, posicao in letras_certas_posicao_errada:
        tabela_letras_erradas[posicao] = letra
    
    return " ".join(resultado), " ".join(tabela_letras_erradas)

def main():     # Função principal do jogo, chama as outras e faz verificação das tentativas até a vitória ou fim de jogo
    palavra_secreta = list(escolher_palavra())
    max_tentativas = len(palavra_secreta) + 2
    letras_certas = []
    letras_certas_posicao_errada = []

    print("Bem-vindo ao Jogo de Adivinhar a Palavra!")
    print(f"A palavra secreta tem 5 letras.\n")
    
    tentativas = 0      # Inicializa o contador das tentativas, sempre antes do laço

    while tentativas < max_tentativas:      # Repete o laço 7 vezes (7 tentativas)
        palavra_oculta, tabela_letras_erradas = mostrar_palavra(palavra_secreta, letras_certas, letras_certas_posicao_errada)
        print(f"{palavra_oculta:<25} -> Palavra secreta")
        print(f"{tabela_letras_erradas:<25} -> Letras certas, posição errada")
        tentativa = input(f"Tentativa {tentativas + 1}/{max_tentativas} (Digite 5 letras): ").strip()
        
        if len(tentativa) != 5:     # Um macete simples, ao invés de fazer uma tratativa de erro com except
            print("Digite exatamente 5 letras.")
            continue
        
        # Essas 4 atribuições foi o chat que fez
        acertos = [(letra, i) for i, letra in enumerate(tentativa) if i < len(palavra_secreta) and letra == palavra_secreta[i]]
        
        letras_certas.extend(acertos)
        
        letras_corretas_erradas = [(letra, i) for i, letra in enumerate(tentativa) if i < len(palavra_secreta) and letra in palavra_secreta and letra != palavra_secreta[i]]
        
        letras_certas_posicao_errada = letras_corretas_erradas
        
        if len(acertos) == len(palavra_secreta):
            print("\nParabéns! Você acertou a palavra!")
            break
        
        tentativas += 1     # Incrementa o contador
    
    if tentativas == max_tentativas:    # Verificação de fim de jogo
        print(f"\nFim de jogo! A palavra secreta era: {''.join(palavra_secreta)} Tente novamente!")

if __name__ == "__main__":
    main()
