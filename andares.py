import os

def clear():
    cont = input(f'\033[0;30;40mcontinuar?[S/N]\033[0m').strip().upper()[0]

    if cont == 'S':
        os.system('cls')
