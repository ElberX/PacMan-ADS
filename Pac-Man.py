if __name__ == '__main__':

    from random import randint
    from time import sleep

    print(20*'\033[1;31m*\033[m')
    print('\33[1;31m*******\033[m\033[1;33mPACMAN\033[m\033[1;31m*******\033[m')
    print(20 * '\033[1;31m*\033[m')
    opcao = int(input('''[ 1 ] INICIAR \n[ 0 ] SAIR \n-> '''))

    while True:
        if opcao == 1:
            print('INICIANDO JOGO...')
            sleep(2)
        elif opcao == 0:
            print('SAINDO...')
            sleep(2)
            break
        elif opcao != 1 and opcao != 0:
            print('ERRO')
            break

        score = 0
        grid = 5
        pacman = '\033[1;33mo\033[m'
        comida = '\033[1;32mX\033[m'
        pontos = '.'

        pacman_pos = [2, 2]
        comida_pos = [randint(0, grid - 1), randint(0, grid - 1)]

        def print_grid():
            for linha in range(grid):
                for col in range(grid):
                    if linha == pacman_pos[0] and col == pacman_pos[1]:
                        print(pacman, end=' ')
                    elif linha == comida_pos[0] and col == comida_pos[1]:
                        print(comida, end=' ')
                    else:
                        print(pontos, end=' ')
                print()

        def move_pacman():
            andar = str(input('Digite W-A-S-D para se movimentar: ')).upper()
            if andar == 'S':
                pacman_pos[0] = (pacman_pos[0] + 1) % grid
            elif andar == 'W':
                pacman_pos[0] = (pacman_pos[0] - 1) % grid
            elif andar == 'D':
                pacman_pos[1] = (pacman_pos[1] + 1) % grid
            elif andar == 'A':
                pacman_pos[1] = (pacman_pos[1]-1) % grid

        while True:

            print_grid()
            move_pacman()

            if pacman_pos == comida_pos:
                score += 1
                if score == 10:
                    print("PONTUAÇÃO: {} \nParabéns! Você venceu".format(score))
                    break
                print("PONTUAÇÃO:", score)

            if pacman_pos == comida_pos:
                comida_pos = [randint(0, grid - 1), randint(0, grid - 1)]

            pacman = '\033[1;31mO\033[m' if pacman == '\033[1;33mo\033[m' else '\033[1;33mo\033[m'
        break
