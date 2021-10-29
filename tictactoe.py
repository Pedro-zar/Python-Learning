import os
isPlaying = True
player1 = ''
rows = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winner = ''
isX = True
wins = [[6, 7, 8], [3, 4, 5], [0, 1, 2], [6, 3, 0],
        [7, 4, 1], [8, 5, 2], [0, 4, 8], [6, 4, 2]]
pontosP1 = 0
pontosP2 = 0
pontosV = 0


def game():
    initialize()
    render()
    while isPlaying:
        tick()
        os.system('cls')
        os.system('clear')
        render()
    endGame()


def endGame():
    global isPlaying, player1, rows, winner
    choise = ''
    print("Pontuação atual:")
    print(f"Jogador 1: {pontosP1}")
    print(f"Jogador 2: {pontosP2}")
    print(f"Velha: {pontosV}")
    while not (choise == "N" or choise == "S"):
        choise = input('Deseja continuar jogando? (S-N)')
    if choise == "N":
        print("Até a próxima")
    else:
        isPlaying = True
        player1 = ''
        rows = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        winner = ''
        game()


def initialize():
    choised = False
    while not choised:
        choice = input('Jogador 1, escolha entre X e O:\n')
        choised = choice.lower() == 'x' or choice.lower() == 'o'
    global player1
    player1 = choice
    if player1 == 'X':
        print('O jogador 1 vai começar jogando')
    else:
        print('O jogador 2 vai começar jogando')


def tick():
    global isX, rows, winner, isPlaying, pontosP1, pontosP2, pontosV
    choised = False
    while not choised:

        if isX:
            player = 'X'
        else:
            player = 'O'
        print(f'Vez do {player}')
        choise = input('Escolha a casa (1-9) para fazer sua jogada:\n')
        if choise.isnumeric():
            if int(choise) > 0 and int(choise) < 10:
                if rows[int(choise)-1] == ' ':
                    choised = True
                    if (isX):
                        rows[int(choise)-1] = 'X'
                    else:
                        rows[int(choise)-1] = 'O'
                    isX = not isX
                else:
                    print('Escolha um espaço não preenchido')
            else:
                print('escolha um número entre 1 e 9')
        else:
            print('insira um número')
    for possibility in wins:
        if rows[possibility[0]] == rows[possibility[1]] == rows[possibility[2]] and rows[possibility[0]] != ' ':
            winner = rows[possibility[0]]
            if winner == player1:
                pontosP1 += 1
            else:
                pontosP2 += 1

    end = True
    for spaces in rows:
        if spaces == " ":
            end = False
    if (end and winner == ""):
        pontosV += 1
        winner = "a Velha, empate"
    if winner != '':
        isPlaying = False


def render():
    print(f'{rows[6]}|{rows[7]}|{rows[8]}')
    print('-----')
    print(f'{rows[3]}|{rows[4]}|{rows[5]}')
    print('-----')
    print(f'{rows[0]}|{rows[1]}|{rows[2]}')
    if winner != '':
        print(f'O ganhador é {winner}')
