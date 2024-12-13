from time import sleep
players = ["Alexandre", "Bernardo", "Diogo Haker", "Daniel", "Edu_ard"]


def comp_print(text, skips):
    for a in str(text):
        print(a, end="")
        sleep(0.1)
    if skips > 0:
        for b in range(int(skips)):
            print()


while True:
    comp_print("⚽ Gestão da equipa SharkCoders🦈", 1)
    print("1: Ver a equipa atual")
    print("2: Substituir um jogador")
    print("3: Adicionar um novo jogador")
    print("4: Remover um jogador")
    print("5: Reorganizar a equipa")
    print("6: Sair")
    print()

    comp_print("Escolhe uma opção: ", 0)
    chose = int(input())
    print()

    if chose == 1:
        comp_print("Equipa atual:", 1)
        for i, p in enumerate(players):
            comp_print(f"{i} - {p}", 1)
    elif chose == 2:
        comp_print("Diz qual destes jogadores queres substituir: ", 0)
        comp_print(players, 1)
        comp_print("Digite a resposta: ", 0)
        pos = input()
        if pos in players:
            comp_print("Digite o nome do novo jogador: ", 0)
            newplayer = input()
            index = players.index(pos)
            players[index] = newplayer
            comp_print("Jogador substituído com sucesso!", 2)
        else:
            print("Jogador inválido. Tente novamente.")
    elif chose == 3:
        comp_print(f"Diz qual jogador queres adicionar: {players}", 1)
        comp_print("Digite a resposta:", 0)
        newplayer = input()
        players.append(newplayer)
        comp_print(f"O seu jogador {newplayer} foi adicionado.")
