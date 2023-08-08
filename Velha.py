import random

def print_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)
def vitoria(tabuleiro , jogador):
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    for i in range(3):
        if all(tabuleiro[i][i] == jogador) or all(tabuleiro[i][2-i] == jogador):
            return True
    return False

def jogo_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador = "X"
    cpu = "0"
    numero_aleatorio1 = random.randint(0 , 2)
    numero_aleatorio2 = random.randint(0 , 2)
    while not fim_jogo:
        print(f"{jogador} , digite sua linha entra [ 0 , 1 , 2] = ")
        linha = int(input())
        print(f"{jogador} , digite sua coluna entre [0 , 1 , 2] = ")
        coluna = int(input())
        if tabuleiro[linha][coluna] == "":
            tabuleiro[linha][coluna] == jogador
            if vitoria(tabuleiro , jogador):
                print(f"Parabens jogador {jogador} , voce ganhou !")
                fim_jogo = True
        else:
                while not liberado:
                    if tabuleiro[numero_aleatorio1][numero_aleatorio2] == "":
                        tabuleiro[numero_aleatorio1][numero_aleatorio2] == cpu
                        if vitoria(tabuleiro , cpu):
                            print("Voce Perdeu !")
                            fim_jogo = True
                        else:
                            liberado = True
                    else:
                        numero_aleatorio1 = random.randint(0 , 2)
                        numero_aleatorio2 = random.randint(0 , 2)

        