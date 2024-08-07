

def arma(player):
    raca = player['raca']
    match raca:
        case 'Humano':
            if player['hp'] > 0:
                print(f'parabens {player['nome']}! você encontrou uma espada longa! \n+30 de ataque')
                player['atk'] += 30
                player['equip'].append('espada longa')

        case 'Orc':
            if player['hp'] > 0:
                print(f'parabens {player['nome']}! você encontrou adagas duplas! \n+20 de atk \n+10 de velocidade')
                player['atk'] += 20
                player['speed'] += 10
                player['equip'].append('adagas duplas')     

        case 'Elfo':
            if player['hp'] > 0:
                print(f'parabens {player['nome']}! você encontrou um arco curto! \n+10 de hp \n+10 de ataque \n+10 de velocidade ')
                player['hp'] += 10
                player['atk'] += 10
                player['speed'] += 10
                player['equip'].append('arco curto')







def escudo(player):
    raca = player['raca']
    match raca:
        case 'Humano':
            if player['hp'] > 0:
                print(f'parabens {player['nome']}! você encontrou um escudo grande! \n+50 de defesa')
                player['defe'] += 50
                player['equip'].append('escudo grande')
            
        case 'Orc':
            if player['hp'] > 0:
                print(f'parabens {player['nome']}! você encontrou um escudo pequeno! \n+5 de hp \n+40 de defesa \n+5 de velocidade')
                player['hp'] += 5
                player['defe'] += 40
                player['speed'] += 5
                player['equip'].append('escudo pequeno')     

        case 'Elfo':
            if player['hp'] > 0:
                print(f'parabens {player['nome']}! você encontrou uma aljava infinita! \n+20 de hp \n+20 de ataque \n+10 de velocidade')
                player['hp'] += 20
                player['atk'] += 20
                player['speed'] += 10
                player['equip'].append('aljava infinita')

                player['ataques'] = {'soco': 1, 'atirar':2, '--': 1, '---': 1}
                print(f"você desbloqueou o ataque: atirar !")

def armadura(player):
    raca = player['raca']
    match raca:
        case 'Humano':
            if player['hp'] > 0:
                print(f'parabens {player['nome']}! você encontrou uma armadura de ferro! \n+100 de hp')
                player['hp'] += 100
                player['equip'].append('armadura de ferro')
            
        case 'Orc':
            if player['hp'] > 0:
                print(f'parabens {player['nome']}! você encontrou uma armadura pesada! \n+25 de hp \n+25 de defesa \n+50 de ataque')
                player['hp'] += 25
                player['defe'] += 25
                player['atk'] += 50
                player['equip'].append('armadura pesada')     

        case 'Elfo':
            if player['hp'] > 0:
                print(f'parabens {player['nome']}! você encontrou uma armadura leve! \n+30 de hp \n+15 de ataque \n+15 de defesa \n+40 de velocidade')
                player['hp'] += 30
                player['atk'] += 15
                player['defe'] += 15
                player['speed'] += 40
                player['equip'].append('armadura leve')

def equipamento(player):
    raca = player['raca']
    match raca:
        case 'Humano':
            if player['hp'] > 0:
                print(f'parabens {player['nome']}! você encontrou breceletes! \n+20 de hp\n+20 de ataque\n+20 de defesa\n+20 de velocidade')
                player['hp'] += 20
                player['atk'] += 20
                player['defe'] += 20
                player['speed'] += 20
                player['equip'].append('breceletes')
            
        case 'Orc':
            if player['hp'] > 0:
                print(f'parabens {player['nome']}! você encontrou ombreiras! \n+15 de hp\n+25 de ataque\n+25 de defesa\n+15 de velocidade')
                player['hp'] += 15
                player['atk'] += 25
                player['defe'] += 25
                player['speed'] += 15
                player['equip'].append('ombreiras')     

        case 'Elfo':
            if player['hp'] > 0:
                print(f'parabens {player['nome']}! você encontrou aneis! \n+10 de hp\n+10 de ataque\n+25 de defesa\n+35 de velocidade')
                player['hp'] += 10
                player['atk'] += 10
                player['defe'] += 25
                player['speed'] += 35
                player['equip'].append('aneis')

def botas(player):
    raca = player['raca']
    match raca:
        case 'Humano':
            if player['hp'] > 0:
                print(f'parabens {player['nome']}! você encontrou botas! \n+200 de velocidade')
                player['speed'] += 200
                player['equip'].append('botas')
            
        case 'Orc':
            if player['hp'] > 0:
                print(f'parabens {player['nome']}! você encontrou botas infernais! \n+100 de hp\n+40 de defesa\n+60 de velocidade')
                player['hp'] += 100
                player['defe'] += 40
                player['speed'] += 60
                player['equip'].append('botas infernais')     

        case 'Elfo':
            if player['hp'] > 0:
                print(f'parabens {player['nome']}! você encontrou botas de trovão! \n+5 de hp\n+195 de velocidade')
                player['hp'] += 5
                player['speed'] += 195
                player['equip'].append('botas de trovão')

def ultima(player):
    raca = player['raca']
    match raca:
        case 'Humano':
            if player['hp'] > 0:
                print(f'parabens {player['nome']}! você despertou seu potencial, sua espada queima e o fogo de sua espada ilumina seu rosto, parabens!')
                player['ataques'] = {'soco': 1, 'espadada':2, 'espadada concentrada': 3, 'corte do amanhecer': 4}
                
            
        case 'Orc':
            if player['hp'] > 0:
                print(f'parabens {player['nome']}! você despertou seu potencial, sua irá domina todo o seu corpo, você se sente controlado pela raiva, parabens!')
                player['ataques'] = {'irá de deuses': 5, 'irá de deuses': 5, 'irá de deuses': 5, 'irá de deuses': 5}
   

        case 'Elfo':
            if player['hp'] > 0:
                print(f'parabens {player['nome']}! você despertou seu potencial, os deuses veem em você o merecedor de tal poder, parabens!')
                player['ataques'] = {'soco': 1, 'atirar':2, 'magia de fogo': 3, 'ULTIMA': 5}
