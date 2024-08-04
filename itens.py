

def espada(player):
    print(f'parabens {player['nome']}! você encontrou uma espada longa! \n+30 de atk')
    player['atk'] += 30
    player['equip'].append('espada longa')

def escudo(player):
    print(f'parabens {player['nome']}! você encontrou um escudo grande! \n+25 de def')
    player['atk'] += 30
    player['equip'].append('espada longa')


