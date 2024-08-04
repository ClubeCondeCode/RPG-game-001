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


slime = [{'nome': 'slime', 'hp': 10, 'atk': 4, 'defe': 3, 'speed': 1, 'level': 1}, 
         {'nome': 'slime', 'hp': 30.0, 'atk': 15.0, 'defe': 9.0, 'speed': 2.2, 'level': 2}, 
         {'nome': 'slime', 'hp': 45.0, 'atk': 22.5, 'defe': 13.5, 'speed': 3.3000000000000003, 'level': 3}, 
         {'nome': 'slime', 'hp': 60.0, 'atk': 30.0, 'defe': 18.0, 'speed': 4.4, 'level': 4}, 
         {'nome': 'slime', 'hp': 75.0, 'atk': 30.0, 'defe': 22.5, 'speed': 5.5, 'level': 5}, 
         {'nome': 'slime', 'hp': 90.0, 'atk': 36.0, 'defe': 27.0, 'speed': 6.6000000000000005, 'level': 6}, 
         {'nome': 'slime', 'hp': 105.0, 'atk': 31.5, 'defe': 31.5, 'speed': 7.700000000000001, 'level': 7}, 
         {'nome': 'slime', 'hp': 120.0, 'atk': 36.0, 'defe': 36.0, 'speed': 8.8, 'level': 8}, 
         {'nome': 'slime', 'hp': 135.0, 'atk': 54.0, 'defe': 40.5, 'speed': 9.9, 'level': 9}, 
         {'nome': 'slime', 'hp': 150.0, 'atk': 45.0, 'defe': 45.0, 'speed': 11.0, 'level': 10}]

troll = [{'nome': 'troll', 'hp': 35, 'atk': 11, 'defe': 8, 'speed': 10, 'level': 1}, 
        {'nome': 'troll', 'hp': 105.0, 'atk': 27.0, 'defe': 21.0, 'speed': 22.0, 'level': 2}, 
        {'nome': 'troll', 'hp': 157.5, 'atk': 45.0, 'defe': 36.0, 'speed': 36.300000000000004, 'level': 3}, 
        {'nome': 'troll', 'hp': 210.0, 'atk': 54.0, 'defe': 36.0, 'speed': 44.0, 'level': 4}, 
        {'nome': 'troll', 'hp': 262.5, 'atk': 82.5, 'defe': 60.0, 'speed': 60.5, 'level': 5}, 
        {'nome': 'troll', 'hp': 315.0, 'atk': 81.0, 'defe': 63.0, 'speed': 66.0, 'level': 6}, 
        {'nome': 'troll', 'hp': 367.5, 'atk': 105.0, 'defe': 73.5, 'speed': 77.00000000000001, 'level': 7}, 
        {'nome': 'troll', 'hp': 420.0, 'atk': 108.0, 'defe': 72.0, 'speed': 96.80000000000001, 'level': 8}, 
        {'nome': 'troll', 'hp': 472.5, 'atk': 135.0, 'defe': 81.0, 'speed': 108.9, 'level': 9},
        {'nome': 'troll', 'hp': 525.0, 'atk': 165.0, 'defe': 90.0, 'speed': 110.0, 'level': 10}]

golem = [{'nome': 'golem', 'hp': 55, 'atk': 12, 'defe': 19, 'speed': 9, 'level': 1}, 
        {'nome': 'golem', 'hp': 165.0, 'atk': 36.0, 'defe': 51.0, 'speed': 8.8, 'level': 2}, 
        {'nome': 'golem', 'hp': 247.5, 'atk': 63.0, 'defe': 85.5, 'speed': 19.8, 'level': 3}, 
        {'nome': 'golem', 'hp': 330.0, 'atk': 84.0, 'defe': 114.0, 'speed': 8.8, 'level': 4}, 
        {'nome': 'golem', 'hp': 412.5, 'atk': 97.5, 'defe': 142.5, 'speed': 16.5, 'level': 5}, 
        {'nome': 'golem', 'hp': 495.0, 'atk': 90.0, 'defe': 135.0, 'speed': 19.8, 'level': 6}, 
        {'nome': 'golem', 'hp': 577.5, 'atk': 115.5, 'defe': 157.5, 'speed': 46.2, 'level': 7}, 
        {'nome': 'golem', 'hp': 660.0, 'atk': 132.0, 'defe': 228.0, 'speed': 17.6, 'level': 8}, 
        {'nome': 'golem', 'hp': 742.5, 'atk': 162.0, 'defe': 243.0, 'speed': 69.3, 'level': 9}, 
        {'nome': 'golem', 'hp': 825.0, 'atk': 195.0, 'defe': 255.0, 'speed': 99.0, 'level': 10}]

dragao = {'nome': 'dragão', 'hp': 1000, 'atk': 200, 'defe': 200, 'speed': 100, 'level': 10}



