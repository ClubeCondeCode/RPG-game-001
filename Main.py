
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


slime_1 = slime[0]
slime_2 = slime[1]
slime_3 = slime[2]
print(status(jogador))

batalha(jogador, slime_1)


arma(jogador)
jogador = upar(player1)

print(status(jogador))

batalha(jogador, slime_2)

jogador = upar(player1)

print(status(jogador))

batalha(jogador, slime_3)








