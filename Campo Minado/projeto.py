from marcaPosicoes import marcaPosicao
import random
import os  # Para usar o clear
def clear(): return os.system('cls')

# // ----------------------------------------------------------------//
#      Escolhe uma das 3 dificuldades (apenas matrizes quadradas)
# // ----------------------------------------------------------------//


def dificuldade():
    print('=====================================')
    print('ESCOLHA A DIFICULDADE: ')
    print('1 - Facil')
    print('2 - Medio')
    print('3 - Dificil')
    existe = False
    while existe == False:
        escolhaDificuldade = int(input())
        if escolhaDificuldade != 1 and escolhaDificuldade != 2 and escolhaDificuldade != 3:
            existe = False
            print('Digite um valor dentro do intervalo 1-3')
        else:
            existe = True

    if escolhaDificuldade == 1:
        return 4
    elif escolhaDificuldade == 2:
        return 5
    else:
        return 15

# // ----------------------------------------------------------------//
#         Contagem de bombas restantes para o fim do jogo
# // ----------------------------------------------------------------//


def bombasRestantes(t, m):
    cont = 0
    for l in range(t):
        for c in range(t):
            if m[l][c] == -1:
                cont = cont + 1
    return cont

# // ----------------------------------------------------------------//
#      Gera um campo aleatório a partir da dificuldade escolhida
# // ----------------------------------------------------------------//


def gerarCampo(t):
    inicial = []
    for l in range(t):
        linha = []
        for c in range(t):
            num = random.randint(-1, 0)
            linha.append(num)
        inicial.append(linha)
    return inicial

# // ----------------------------------------------------------------//
#                       Mostra a matriz
# // ----------------------------------------------------------------//


def mostrarMatriz(t, m):
    for i in range(t):
        for j in range(t):
            print(' '*4, f'{m[i][j]:^3}', ' ', end='')
        print('')

# // ----------------------------------------------------------------//
#                 Matriz padrão apenas com '-'
# // ----------------------------------------------------------------//


def default(t):
    campoVazio = []
    for l in range(t):
        linha = []
        for c in range(t):
            linha.append('#')
        campoVazio.append(linha)
    return campoVazio

# // ----------------------------------------------------------------//
#          Computa a quantidade de bombas no jogo atual
# // ----------------------------------------------------------------//


def computaBombas(m):
    matrizM = []
    for linha in range(len(m)):
        matrizM.append([])
        for coluna in range(len(m[linha])):
            if m[linha][coluna] == -1:
                matrizM[linha].append(-1)
                continue
            matrizM[linha].append(contaQtdMenosUm(m, linha, coluna))
    return matrizM


def contaQtdMenosUm(m, i, j):
    cont = 0
    for linha in range(len(m)):
        for coluna in range(len(m[linha])):
            if linha == i and coluna == j:
                continue
            if m[linha][coluna] == -1:
                if linha == (i - 1) and (coluna == (j-1) or coluna == j or coluna == (j+1)):
                    cont = cont + 1
                elif linha == i and (coluna == j - 1 or coluna == j + 1):
                    cont = cont + 1
                elif linha == i + 1 and (coluna == j - 1 or coluna == j or coluna == j + 1):
                    cont = cont + 1
    return cont

# // ----------------------------------------------------------------//
#                              MAIN
# // ----------------------------------------------------------------//


def main():
    tamanho = dificuldade()                # Tamanho do campo
    # Primeiro campo gerado, utilizado para elaboração das outras matrizes
    matriz = gerarCampo(tamanho)
    # Computa o total de bombas no campo gerado
    contBombas = bombasRestantes(tamanho, matriz)
    # Campo vazio inicial preenchido "#" que será alterado futuramente
    campoVazio = default(tamanho)
    campoAtual = campoVazio                # Campo que será modificado pelo usuário
    # Campo com as posições e números computados
    campoComputado = computaBombas(matriz)
    fimDeJogo = False
    posicoesParaDescobrir = tamanho * tamanho - contBombas
    while not fimDeJogo:
        clear()
        mostrarMatriz(tamanho, campoAtual)
        jogadaJafeita = True
        while jogadaJafeita == True:
            linha = int(input("Digite a linha que deseja marcar: ")) - 1
            coluna = int(input("Digite a coluna que deseja marcar: ")) - 1
            if campoAtual[linha][coluna] != '#':
                jogadaJafeita = True
                print('Voce ja jogou nesta posicao! Tente outra vez!')
            else:
                jogadaJafeita = False
        puxarCont = False
        campoAtual = marcaPosicao(
            campoAtual, campoComputado, linha, coluna, tamanho, puxarCont)
        puxarCont = True
        contagem = marcaPosicao(
            campoAtual, campoComputado, linha, coluna, tamanho, puxarCont)
        posicoesParaDescobrir = posicoesParaDescobrir - contagem
        if campoAtual[linha][coluna] == -1:
            clear()
            fimDeJogo = True
            print('')
            print('XXX===============================XXX')
            print('    Clicou na bomba! Voce perdeu!')
            print('XXX===============================XXX')
            print('')
        else:
            if posicoesParaDescobrir == 0:
                clear()
                fimDeJogo = True
                print('')
                print('!!!===============================!!!')
                print('           Voce venceu!')
                print('!!!===============================!!!')
                print('')
    mostrarMatriz(tamanho, campoAtual)
    print('')
    print('-------------------------------------------------')
    print('')
    mostrarMatriz(tamanho, campoComputado)


# // ----------------------------------------------------------------//
#                      Ativação do programa
# // ----------------------------------------------------------------//
main()
