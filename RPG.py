from personagem import playerStatus

print('\033[32mBem vindo ao mundo de\033[0m \'\033[1m\033[31mA Descida do Abismo\033[0m\033[0m\' ')

jogar = input('Você quer entrar no mundo de \033[0m \'\033[1m\033[31mA Descida do Abismo\033[0m\033[0m\' S/N? ').strip().upper()

if jogar == 'S':
    campanha = input('Iniciar nova campanha: iniciar \nCarregar campanha: carregar\n ').strip().lower()
    
    if campanha == 'iniciar':
        nome = input('Digite seu nome: ').strip()

        status_jogador = playerStatus(nome)
        
        print(f"Status do jogador: \nNome: {status_jogador[0]}\nHP: {status_jogador[1]}\nMP: {status_jogador[2]}\natk: {status_jogador[3]}\nDef: {status_jogador[4]}")
    else:
        print('Opção não reconhecida. Encerrando o jogo.')
else:
    print('Volte sempre')
