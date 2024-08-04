

def arma(player):
    raca = player['raca']
    match raca:
        case 'Humano':
            print(f'parabens {player['nome']}! você encontrou uma espada longa! \n+30 de ataque')
            player['atk'] += 30
            player['equip'].append('espada longa')

        case 'Orc':
            print(f'parabens {player['nome']}! você encontrou uma adagas duplas! \n+20 de atk \n+10 de velocidade')
            player['atk'] += 20
            player['speed'] += 10
            player['equip'].append('adagas duplas')     

        case 'Elfo':
            print(f'parabens {player['nome']}! você encontrou um arco curto! \n+10 de hp \n+10 de ataque \n+10 de velocidade ')
            player['hp'] += 10
            player['atk'] += 10
            player['speed'] += 10
            player['equip'].append('arco curto')



def escudo(player):
    raca = player['raca']
    match raca:
        case 'Humano':
            print(f'parabens {player['nome']}! você encontrou um escudo grande! \n+50 de defesa')
            player['defe'] += 50
            player['equip'].append('escudo grande')
            
        case 'Orc':
            print(f'parabens {player['nome']}! você encontrou um escudo pequeno! \n+5 de hp \n+40 de defesa \n+5 de velocidade')
            player['hp'] += 5
            player['defe'] += 40
            player['speed'] += 5
            player['equip'].append('escudo pequeno')     

        case 'Elfo':
            print(f'parabens {player['nome']}! você encontrou uma aljava infinita! \n+20 de hp \n+20 de ataque \n+10 de velocidade')
            player['hp'] += 20
            player['atk'] += 20
            player['speed'] += 10
            player['equip'].append('aljava infinita')

            player['ataques'] = {'soco': 1, 'atirar':2, '--': 1, '---': 1}


