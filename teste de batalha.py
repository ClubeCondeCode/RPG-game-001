from random import randrange
from time import sleep
import os


player = {
    'nome':'joao',
    'hp': randrange(10, 20),
    'atk': 3,
    'def': 5,
    'speed': randrange(1, 3)
}

enemy = {
    'nome':'Otavio',
    'hp': randrange(8, 16),
    'atk': 2,
    'def': 3,
    'speed': randrange(1, 5)
}
if player['speed'] > enemy['speed']:
    mais_rapido = player
    mais_lento = enemy
else:
    mais_rapido = enemy
    mais_lento = player
    
while True:
    print(f"{mais_rapido['nome']} atacou {mais_lento['nome']}")
    sleep(1)
    print(f"{mais_lento['nome']} tomou {mais_rapido['atk']} de dano")
    mais_lento['hp'] -= mais_rapido['atk']
    sleep(1)
    print(f"{mais_lento['nome']} esta com {mais_lento['hp']} de hp")
    sleep(1)
    
    os.system('clear')
    
    print(f"{mais_lento['nome']} atacou {mais_rapido['nome']}")
    sleep(1)
    print(f"{mais_rapido['nome']} tomou {mais_lento['atk']} de dano")
    mais_rapido['hp'] -= mais_lento['atk']
    sleep(1)
    print(f"{mais_rapido['nome']} esta com {mais_rapido['hp']} de hp")
    sleep(1)
    
    if mais_rapido['hp'] <= 0:
        perdedor = mais_rapido
        break
    if mais_lento['hp'] <= 0:
        perdedor = mais_lento
        break
    
print(f"{perdedor['nome']} morreu")
