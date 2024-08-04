
from random import randrange
import json

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


slime = slime[0]

batalha(jogador, slime)





