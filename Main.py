
from random import randrange
import json

from monstros import slime
from jogador import dano, player, upar, batalha

salvar = input('''
[1] novo jogo
[2] carregar
               
digite aqui: ''')

if salvar == '1':
    player1 = player()
    jogador = player1
    save = open("save.json", "w")
    json.dump(jogador, save)


if salvar == '2':
    save = open("save.json", "r")
    jogador = json.load(save)

print(jogador)

batalha(jogador, slime)







