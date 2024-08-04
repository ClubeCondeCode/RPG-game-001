from random import randrange


def monstro(nome, hp, atk, defe, speed, andar):
    

    if andar > 1:
        hp *= andar * 1.5
        atk *= andar * 1.5
        defe *= andar * 1.5
        speed *= andar * 1.1

    status = {
        'nome': nome,
        'hp': hp,
        'atk': atk,
        'defe': defe,
        'speed': speed,
        'level': andar
    }


    return status


slime = monstro('slime', 10, randrange(3, 6), 3, 1, 1)
