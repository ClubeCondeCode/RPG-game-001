from time import sleep
from random import randrange
import json

from andares import clear
from monstros import slime, troll, golem
from jogador import player, upar, batalha, status, salvar, carregar
from itens import arma, escudo, gosma

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

#andar 1
slime_1 = slime[0]
troll_1 = troll[0]
golem_1 = golem[0]


if jogador['andar'] == 1: 
    print(f'\033[0;30;40mbem vindo \033[0;32;40m{jogador['nome']}\033[0m\033[0;30;40m! você é um soldado do exercito que foi enviado a essa dungeon em busca de tesouros e poder!')
    #sleep(3)
    print(f'\033[0;30;40mseus status são: {status(jogador)}')
    input('aperte algo para continuar')
    clear()
    print('\033[0;30;40mAssim que você adentra no primeiro andar dessa dungeon, a iluminação mostra um ser pulando em sua direção\033[0m')
    #sleep(3)
    batalha(jogador, slime_1)
    gosma(jogador)
    
    print(f'\033[0;30;40mseus status são: {status(jogador)}')
    batalha(jogador, troll_1)
    #sleep(3)
    
    

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







