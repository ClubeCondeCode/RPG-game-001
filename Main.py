from time import sleep
from random import randrange
import json

from andares import clear
from monstros import slime
from jogador import player, upar, batalha, status, salvar, carregar
from itens import arma, escudo

#sistema de save
#-------------------------------------------------------------------------------------
save = input('''
[1] novo jogo
[2] carregar
               
digite aqui: ''')

if save == '1':
    player1 = player()
    jogador = player1

    salvar(player1, jogador)

if save == '2':
    player1 = carregar('save1.json')
    jogador = carregar('save2.json')

#--------------------------------------------------------------------------------------


slime_1 = slime[0]
slime_2 = slime[1]
slime_3 = slime[2]

if jogador['andar'] == 1:
    print(f'\033[0;30;40mbem vindo \033[0;32;40m{jogador['nome']}\033[0m\033[0;30;40m! você é um soldado do exercito que foi enviado a essa dungeon em busca de tesouros e poder!')
    sleep(3)
    print(f'\033[0;30;40mseus status são: {status(jogador)}')
    clear()

    

'''print(status(jogador))

batalha(jogador, slime_1)


arma(jogador)
jogador = upar(player1)

print(status(jogador))

batalha(jogador, slime_2)

jogador = upar(player1)

print(status(jogador))

batalha(jogador, slime_3)
'''







