from random import randrange

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
        if raca == 2:
            hp = randrange(19, 25)
            atk = randrange(7, 11)
            defe = randrange(4, 7)
            speed = randrange(1, 5)
        if raca == 3:
            hp = randrange(12, 17)
            atk = randrange(5, 9)
            defe = randrange(1, 4)
            speed = randrange(7, 11)


        status = {
        'nome': nome,
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

        player['andar'] += 1

        status = {
    'nome':player['nome'],
    'hp':player['hp'] + player['andar'] * 1.5,
    'atk':player['atk'] + player['andar'] * 1.5,
    'defe':player['defe'] + player['andar'] * 1.5,
    'speed':player['speed'] + player['andar'] * 1.5,
    'andar': player['andar'],
    'ataques': {'soco': 1, '-':1, '--':1, '---':1},
    'equip': equip,
    'inventario': inv
        }

        if player['andar'] >= 4:
            status['andar'] = {'soco': 1, 'chute':2, '--': 1, '---': 1}



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
andar:       {player['andar']}
hp:          {player['hp']}
ataque:      {player['atk']}
defesa:      {player['defe']}
velocidade:  {player['speed']}
equipamentos: {[c for c in player['equip']]}
"""
    return texto


def batalha(player, monstro):
    print(f"você encontrou um {monstro['nome']}")
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
                            print('você fugiu! ')
                            break

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
                        print('você fugiu! ')
                        break
                

                
                     
                


