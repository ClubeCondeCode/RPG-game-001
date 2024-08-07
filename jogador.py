from random import randrange
from time import sleep
from math import trunc
import json
from andares import clear

def salvar(fix, var):
    save1 = open("save1.json", "wt")
    save2 = open("save2.json", "wt")

    json.dump(fix, save1)
    json.dump(var, save2)

def carregar(file):
        valor = open(file, "r")
        save = json.load(valor)
        return save


def player(andar = 1):
        nome = str(input('Digite seu nome: ')).strip().capitalize()
        raca = int(input('''
    Qual raça você escolherá?
        [1] humano
        [2] orc
        [3] elfo

    '''))
        if raca == 1:
            hp = randrange(15, 20)
            atk = randrange(4, 7)
            defe = randrange(2, 5)
            speed = randrange(3, 8)
            raca = 'Humano'
        if raca == 2:
            hp = randrange(19, 25)
            atk = randrange(7, 11)
            defe = randrange(4, 7)
            speed = randrange(1, 5)
            raca = 'Orc'
        if raca == 3:
            hp = randrange(12, 17)
            atk = randrange(5, 9)
            defe = randrange(1, 4)
            speed = randrange(7, 11)
            raca = 'Elfo'


        status = {
        'nome': nome,
        'raca': raca,
        'hp': hp,
        'atk': atk,
        'defe': defe,
        'speed': speed,
        'andar': andar,
        'ataques': {'soco': 1, '-':1, '--':1, '---':1},
        'equip':[],
        'inventario':[]

        }




        return status

def upar(player):
        inv = player['inventario']
        equip = player['equip']
        raca = player['raca']
        ataques = player['ataques']

        player['andar'] += 1

        status = {
    'nome':player['nome'],
    'hp':player['hp'] + player['hp'] * 0.5,
    'raca': raca,
    'atk':player['atk'] + player['atk'] * 0.5,
    'defe':player['defe'] + player['defe'] * 0.5,
    'speed':player['speed'] + player['speed'] * 0.5,
    'andar': player['andar'],
    'ataques': ataques,
    'equip': equip,
    'inventario': inv
        }
        
        if player['andar'] >= 2:
            if player['raca'] == 'Humano':
                status['ataques'] = {'soco': 1, 'espadada':2, '--': 1, '---': 1}
            if player['raca'] == 'Orc':
                status['ataques'] = {'soco': 1, 'golpe pesado':2, '--': 1, '---': 1}

        if player['andar'] >= 5:
            if player['raca'] == 'Elfo':
                status['ataques'] = {'soco': 1, 'atirar':2, 'magia de fogo': 3, '---': 1}
            if player['raca'] == 'Orc':
                status['ataques'] = {'soco': 1, 'golpe pesado':2, 'golpe cortante': 3, '---': 1}

        if player['andar'] >= 7:
            if player['raca'] == 'Orc':
                status['ataques'] = {'soco': 1, 'golpe pesado':2, 'golpe cortante': 3, 'Golpe gigante': 4}
            if player['raca'] == 'Humano':
                status['ataques'] = {'soco': 1, 'espadada':2, 'espadada concentrada': 3, '---': 1}

        if player['andar'] >= 10:
            print()

        salvar(status, status)


        return status


def dano(player, monstro, ataque):
    ataque = player['ataques'][ataque]
    dano = (player['atk'] - monstro['defe']) * ataque
    if dano <= 0:
        dano = 1

    return dano

def tomar_dano(player, monstro):
    dano = monstro['atk'] - player['defe']
    if dano <= 0:
        dano = 1

    return dano

def mais_rapido(player, monstro):
    if player['speed'] >= monstro['speed']:
        mais_rapido = player
        
    else:
        mais_rapido = monstro
    
    return mais_rapido

def status(player):
    texto = f"""
\033[0;37;40m
nome:        {player['nome']}
andar:       {player['andar']}
raça:        {player['raca']}
hp:          {trunc(player['hp'])}
ataque:      {trunc(player['atk'])}
defesa:      {trunc(player['defe'])}
velocidade:  {trunc(player['speed'])}
equipamentos: {[c for c in player['equip']]}\033[0m
"""
    return texto


def batalha(player, monstro):
    print(f"\033[0;30;40mvocê encontrou um \033[0;36;40m{monstro['nome']}\033[0m")
    while True:   
        primeiro = mais_rapido(player, monstro)

        if True:
            if player['hp'] <= 0:
                print('game over')
                break

            if monstro['hp'] <= 0:
                print(f'você matou o {monstro['nome']}')
                break

            if primeiro == player:
                    acao = int(input(f"Oque você ira fazer? \n[1] atacar \n[2] usar item \n[3] fugir\nDigite aqui: "))
                    clear()

                    if acao == 1:
                        ataque = input(f'qual ataque você usara? \n{list(player['ataques'].keys())[0]} \n{list(player['ataques'].keys())[1]} \n{list(player['ataques'].keys())[2]} \n{list(player['ataques'].keys())[3]} \nDigite aqui: ')

                        monstro['hp'] -= dano(player, monstro, ataque)

                        print(f"{player['nome']} usou {ataque} e deu {dano(player, monstro, ataque)} de dano")
                        print(f"{monstro['nome']} esta com {monstro['hp']} hp")
 
                    #inventario
                    if acao == 2:
                        if len(player['inventario']) == 0:
                            print('você não possui itens. ')
                            continue
                        
                        elif len(player['inventario']) > 0:
                            print('qual item você usara? ')
                            for c, i in enumerate(player['inventario']):
                                print(f'{c} - {i}')

                            item_num = int(input('digite aqui: '))
                            item = player['inventario'][item_num]

                            print(f'você usou {item}!')
                            if item == 'poção':
                                player['hp'] += 20
                                print('o jogador recuperou 20 de hp! ')
                                player['inventario'].pop(item_num)

                            if item == 'gosma de slime':
                                player['hp'] += 5
                                print('o jogador recuperou 5 de hp! ')
                                player['inventario'].pop(item_num)

                    print(f'você esta com {player['hp']}')


                    if acao == 3:
                        chance = randrange(0, 100)
                        if chance >= 80:
                            print("você tentou fugir e... você fugiu!")
                            break
                        if chance < 80:
                            print("você tentou fugir e... não conseguiu!")
                        

                    player['hp'] -= tomar_dano(player, monstro)
                    print(f"você tomou {tomar_dano(player, monstro)} de dano")
                     
            elif primeiro == monstro:
                player['hp'] -= tomar_dano(player, monstro)
                print(f"você tomou {tomar_dano(player, monstro)} de dano")
                acao = int(input(f"Oque você ira fazer? \n[1] atacar \n[2] usar item \n[3] fugir\nDigite aqui: "))

                if acao == 1:
                    ataque = input(f'qual ataque você usara? \n{list(player['ataques'].keys())[0]} \n{list(player['ataques'].keys())[1]} \n{list(player['ataques'].keys())[2]} \n{list(player['ataques'].keys())[3]} \nDigite aqui: ')

                    monstro['hp'] -= dano(player, monstro, ataque)

                    print(f"{player['nome']} usou {ataque} e deu {dano(player, monstro, ataque)} de dano")
                    print(f"{monstro['nome']} esta com {monstro['hp']} hp")

                #inventario
                if acao == 2:
                    if len(player['inventario']) == 0:
                        print('você não possui itens. ')
                        continue
                    
                    elif len(player['inventario']) > 0:
                        print('qual item você usara? ')
                        for c, i in enumerate(player['inventario']):
                            print(f'{c} - {i}')
                        item = int(input('digite aqui: '))
                        item = player['inventario'][item]

                        print(f'você usou {item}!')
                        if item == 'poção':
                            player['hp'] += 20
                            print('o jogador recuperou 20 de hp! ')
                if acao == 3:
                    chance = randrange(0, 100)
                    if chance >= 80:
                        print("você tentou fugir e...", end=' ')

                        sleep(1)

                        print("você fugiu!")
                        break
                    if chance < 80:
                        print("você tentou fugir e...", end=' ')
                        sleep(1)
                        print("não conseguiu!")

                
'''

'''
                


