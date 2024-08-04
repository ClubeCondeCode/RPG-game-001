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
        'ataques': {'soco': 1, }

        }




        return status

def upar(player):
        player['andar'] += 1

        status = {
             
    'nome':player['nome'],
    'hp':player['hp'] + player['andar'] * 1.5,
    'atk':player['atk'] + player['andar'] * 1.5,
    'defe':player['defe'] + player['andar'] * 1.5,
    'speed':player['speed'] + player['andar'] * 1.5,
    'andar': player['andar'],
    'ataques': {'soco': 1, }

        }



        return status


def dano(player, monstro):
    dano = player['atk'] - monstro['defe']
    if dano <= 0:
        dano = 1

    return dano

def tomar_dano(player, monstro):
    dano = monstro['atk'] - player['defe']
    if dano <= 0:
        dano = 1

    return dano

def batalha(player, monstro):

    

     


    


